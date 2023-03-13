'''
Auto checkin
'''
import datetime
import re
import requests
import time


def time_stamp():
    '''
    return time stamp
    '''
    return time.strftime("%m-%d %H:%M:%S", time.localtime())

def login(url, data, proxy=None):
    '''
    Login website and return cookie
    '''
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("使用代理")
        response = requests.post(url, data=data, proxies=proxy)
    return response.cookies

if __name__ == '__main__':
    proxy = {'http': 'socks5://127.0.0.1:1080', 'https': 'socks5://127.0.0.1:1080'}
    URL_HOST = 'HOSTNAME'
    URL_HOME = URL_HOST + '/user'
    URL_LOGIN = URL_HOST + '/auth/login'
    URL_CHECKIN = URL_HOST + '/user/checkin'
    LOGIN_DATA = {
        "email": 'EMAIL',
        "passwd": 'PASSWORD',
        "remember_me": "week",
    }
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    }
    # 签到间隔时间(分)
    INTERVAL_CHECKIN = datetime.timedelta(minutes=60*22)
    # 失败重试次数
    RETRY = 5
    # 失败重试等待时间(秒)
    RETRY_WAIT = 5
    # 防爆破延迟时间(秒)
    DELAY_WAIT = 5
    CHECKIN_STATE = 0
    cookies = login(URL_LOGIN, LOGIN_DATA, proxy)
    while True:
        response = requests.get(URL_HOME, headers=headers, cookies=cookies)
        if response.status_code != 200:
            response = requests.get(URL_HOME, headers=headers, cookies=cookies, proxies=proxy)
        response = response.content.decode("utf-8")
        time_last_checkin = re.search(
            r"(?<=<p>上次签到时间：<span class=\"badge bg-green\">).*(?=</span>)", response)
        if time_last_checkin is None:
            print(time_stamp(), "重获取 Cookies")
            cookies = login(URL_LOGIN, LOGIN_DATA)
            time.sleep(DELAY_WAIT)
            continue
        time_last_checkin = datetime.datetime.strptime(
            time_last_checkin[0], '%Y-%m-%d %H:%M:%S')
        time_now = datetime.datetime.now()
        time_interval = time_now-time_last_checkin
        if time_interval < INTERVAL_CHECKIN:
            if CHECKIN_STATE:
                print(time_stamp(), "签到成功")
                CHECKIN_STATE = 0
            print(time_stamp(), "上次签到时间: ", time_last_checkin)
            print(time_stamp(), "下次签到时间: ",
                  (INTERVAL_CHECKIN-time_interval).seconds, "秒后")
            time.sleep((INTERVAL_CHECKIN-time_interval).seconds)
        else:
            if CHECKIN_STATE != 0:
                print(time_stamp(), "签到失败", CHECKIN_STATE, "次")
                time.sleep(DELAY_WAIT)
                if CHECKIN_STATE > RETRY:
                    print(time_stamp(), "签到连续失败，等待后重试...")
                    CHECKIN_STATE = 0
                    time.sleep(RETRY_WAIT)
            print(time_stamp(), "开始签到")
            response = requests.post(URL_CHECKIN, headers=headers, cookies=cookies)
            if response.status_code != 200:
                response = requests.post(URL_CHECKIN, headers=headers, cookies=cookies, proxies=proxy)
            CHECKIN_STATE += 1
