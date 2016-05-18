import urllib.request
import time
import random
room = input('Room ID:')
if len(room) == 0:
    room = 43508
text = input('Danmaku(Enter to exit):')
data = []
while text != '':
    data.append(text)
    text = input('Danmaku(Enter to exit):')
if len(data) == 0:
    data = ['Bilibili~~', ]
k = 0
i = input('Cycles(-1 to Endless loop):')
if len(i) == 0:
    i = -1
i = int(i)
start_hour = input('Start hour:')
if len(start_hour) == 0:
    start_hour = 0
start_hour = int(start_hour)
start_min = input('Start minute:')
if len(start_min) == 0:
    start_min = 0
start_min = int(start_min)
request = urllib.request.Request("http://live.bilibili.com/msg/send")
# file = open(r'Cookie.txt')
# cookie = file.read()
cookie = 'DedeUserID=???; DedeUserID__ckMd5=???; SESSDATA=???;'
request.add_header('Cookie', cookie)
while i != 0:
    min = time.localtime()[4]
    if min >= start_min:
        print(time.localtime()[3], ':', time.localtime()[4], 'Start')
    while min >= start_min:
        if k >= len(data):
            k = 0
            min = time.localtime()[4]
        dm = str(data[k] + str(int(random.uniform(100, 1056))))
        if len(dm) >= 20:
            continue
        post = 'color=16777215&fontsize=25&mode=1&msg=%s&rnd=1463234970&roomid=%s' % (
            dm, room)
        post = post.encode('utf-8')
        # urllib.request.urlopen(request, post)
        print(dm)
        k += 1
        time.sleep(random.uniform(0.5, 1.5))
    print(time.localtime()[3], ':', time.localtime()[4], 'End')
    i -= 1
    time.sleep(60)
print('Exit!!!')
