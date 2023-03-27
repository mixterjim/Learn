import requests
import sys

MAX_IMAGES = 100
USER_ID = "1842706721"
SUB_COOKIE = "_2AkMTRtWxf8NxqwJRmPoRzGPqaYl-zw3EieKlGiRqJRMxHRl-yT9kqhwctRB6OMb7XsPta_FgFKRN1pV2fWB65ptol6RY"

HEADERS = {
    'Referer': f'https://weibo.com/u/{USER_ID}?tabtype=album',
    'cookie': f'SUB={SUB_COOKIE}'
}
IMAGE_WALL_URL = f"https://weibo.com/ajax/profile/getImageWall?uid={USER_ID}"


def fetch_image_wall(url: str) -> None:
    """
    Fetch image wall recursively and get image PIDs.
    """
    response = requests.get(url, headers=HEADERS)
    try:
        data = response.json()['data']
    except requests.exceptions.JSONDecodeError:
        print("Error: Probably a cookie error")
        sys.exit()
    save_image_pids(data['list'])
    since_id = data['since_id']
    if since_id == 0:
        return
    next_url = f"{IMAGE_WALL_URL}&sinceid={since_id}"
    fetch_image_wall(next_url)


def save_image_pids(image_list: list) -> None:
    """
    Save image download URLs to a file.
    """
    with open(f'{USER_ID}.txt', 'a+') as file:
        for image in image_list:
            file.write(f"{generate_download_url(image['pid'])}\n")


def get_download_url_func() -> callable:
    count = 0

    def download_url(pid: str) -> str:
        """
        Return image download URL and exit if count exceeds MAX_IMAGES.
        """
        nonlocal count
        count += 1
        if MAX_IMAGES != 0 and count > MAX_IMAGES:
            print("Finish: MAX_IMAGES")
            sys.exit()
        image_url = f"https://wx{count % 4 + 1}.sinaimg.cn/large/{pid}.jpg"
        print(f"{count}: {image_url}")
        return image_url
    return download_url


generate_download_url = get_download_url_func()
fetch_image_wall(IMAGE_WALL_URL + "&sinceid=0")
