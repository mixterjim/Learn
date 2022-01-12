"""
Read the URL title from the CSV and save it.
"""
import re
import csv
import sys
import time
import threading
import requests


def print_time_stamp(func):
    """
    @print_time_stamp
    """
    def inner(*args, **kwargs):
        print(time.strftime("%m-%d %H:%M:%S", time.localtime()), end=" ")
        return func(*args, **kwargs)
    return inner


class ThreadWithReturnValue(threading.Thread):
    """
    Modify threading to return the function return value
    """

    def __init__(self, group=None, target=None, name=None, args=()):
        threading.Thread.__init__(self, group, target, name, args)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return


def get_url_title(url, timeout=5) -> str:
    """
    Regular match page to get title
    """
    # fuction_name = sys._getframe(1).f_code.co_name
    fuction_name = "GetUrlTitle"
    try:
        headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        }
        response = requests.get(url, headers=headers, timeout=timeout)
    except requests.exceptions.Timeout:
        line = sys._getframe().f_lineno
        _title = f"WARRING/{fuction_name}({line}): Timeout"
    except requests.exceptions.RequestException:
        line = sys._getframe().f_lineno
        _title = f"ERROR/{fuction_name}({line}): requests.get"
    else:
        try:
            # 获取网页编码
            charset = response.content.decode("utf-8", errors='ignore')
            charset = re.search(r"(?<=charset)[^>]*", charset)
            if charset:
                charset = charset[0]
            else:
                charset = "utf-8"
            response = response.content.decode(charset, errors='ignore')
            # 匹配标题标签，包括换行符
            _title = re.search(r"<title([\s\S]*)</title>", response)[0]
            # 替换标题内换行符和空格
            _title = re.sub(r"\s", "_", _title)
            _title = re.search(r"(?<=>).*(?=<)", _title)[0]
        except TypeError:
            line = sys._getframe().f_lineno
            _title = f"ERROR/{fuction_name}({line}): 正则匹配失败"
    finally:
        time_stamp = time.strftime("%m-%d %H:%M:%S", time.localtime())
        # 线程安全
        sys.stdout.write(time_stamp + " " + _title + '\n')
        threadMax.release()
    return _title

if __name__ == '__main__':
    FILENAME = "BrowsingHistory.csv"
    # 数据所在行
    COLUMN = 1
    # 超时时间
    TIMEOUT = 5
    # 限制线程数量
    # Deprecated since version 3.8, removed in version 3.10
    threadMax = threading.BoundedSemaphore(50)
    with open(FILENAME, mode="r", encoding="utf_8_sig") as csvFile:
        csvReader = csv.reader(csvFile)
        rows = []
        threads = []
        for row in csvReader:
            rows.append(row)
            threadMax.acquire()
            threads.append(ThreadWithReturnValue(target=get_url_title, args=(row[COLUMN], TIMEOUT)))
            threads[-1].start()
        for i in range(len(threads)):
            title = threads[i].join()
            rows[i].append(title)

    input("输入回车保存并退出")
    with open(FILENAME, mode="w", newline='', encoding="utf_8_sig") as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(rows)
