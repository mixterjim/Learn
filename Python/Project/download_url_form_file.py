import os
import requests

headers = {'Referer': 'https://weibo.com/u/7091264504?tabtype=album'}

input_file_name = '1.txt'
download_folder_name = os.path.splitext(input_file_name)[0]

if not os.path.exists(download_folder_name):
    os.makedirs(download_folder_name)

# Count the number of images in the input file
with open(input_file_name, 'r') as file:
    num_images = sum(1 for line in file)

# Download each image and update the counter
with open(input_file_name, 'r') as file:
    image_counter = 0
    for url in file:
        url = url.strip()
        filename = os.path.join(download_folder_name, url.split('/')[-1])
        response = requests.get(url, headers=headers, stream=True)
        total_size_in_bytes = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 KB
        with open(filename, 'wb') as f:
            for data in response.iter_content(block_size):
                f.write(data)
        image_counter += 1
        print(f"Downloaded image {image_counter} of {num_images}")
