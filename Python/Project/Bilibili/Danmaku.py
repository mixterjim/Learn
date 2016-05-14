import urllib.request
room = input('请输入房间ID:')
if len(room) == 0:
    room = 43508
text = input('请输入弹幕内容:')
if len(text) == 0:
    text = '神级刷屏'
num = 0  # 防止短时间发送相同内容弹幕会被屏蔽
i = int(input('请输入循环次数(负数为无限循环):'))
if len(i) == 0:
    i = -1
request = urllib.request.Request("http://live.bilibili.com/msg/send")
file = open(r'Cookie.txt')
cookie = file.read()
# cookie = 'DedeUserID=???; DedeUserID__ckMd5=???; SESSDATA=???;'
request.add_header('Cookie', cookie)
while i != 0:
    dm = text + str(num)
    data = 'color=16777215&fontsize=25&mode=1&msg=%s&rnd=1463234970&roomid=%s' % (
        dm, room)
    data = data.encode('utf-8')
    urllib.request.urlopen(request, data)
    if len(dm) >= 20:
        num = 0
    num += 1
    i -= 1
