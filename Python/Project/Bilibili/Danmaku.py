import urllib.request
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
num = 0
k = 0
i = input('Cycles(-1 to Endless loop):')
if i == '':
    i = -1
i = int(i)
request = urllib.request.Request("http://live.bilibili.com/msg/send")
# file = open(r'Cookie.txt')
# cookie = file.read()
cookie = 'DedeUserID=???; DedeUserID__ckMd5=???; SESSDATA=???;'
request.add_header('Cookie', cookie)
print('Start')
while i != 0:
    if k >= len(data):
        k = 0
    dm = str(data[k]+str(num))
    post = 'color=16777215&fontsize=25&mode=1&msg=%s&rnd=1463234970&roomid=%s' % (
        dm, room)
    post = post.encode('utf-8')
    urllib.request.urlopen(request, post)
    if len(dm) >= 20:
        num = 0
    num += 1
    i -= 1
    k += 1
print('End')
