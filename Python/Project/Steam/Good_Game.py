from urllib import request
from re import findall
from pandas import DataFrame
# urllib.request.urlopen(url, data=None, [timeout,]* cafile=None, capath=None, cadefault=False, context=None)
html = request.urlopen('http://steamcommunity.com/id/mixterjim/games/?tab=all')
data = html.read().decode('utf-8')
id = findall(r'(?<=appid":)\d+', data)
name = findall(r'(?<="name":").*?(?=","logo")', data)
frame = DataFrame({'name': name, 'id': id, 'good': None, 'bad': None})
i = 0
score = {'good': [], 'bad': []}
while i < len(frame):
    req = request.Request('http://store.steampowered.com/app/%s/?cc=us' % (frame.id[i]))
    req.add_header('Cookie', 'birthtime=-2209016279;')
    html2 = request.urlopen(req)
    data2 = str(html2.read())
    good = findall(r'(?<=Positive </span> <span class="user_reviews_count">\().*?(?=\))', data2)
    if good == []:
        i += 1
        continue
    frame.good[i] = int(good[0].replace(',', ''))
    bad = findall(r'(?<=Negative </span> <span class="user_reviews_count">\().*?(?=\))', data2)
    frame.bad[i] = int(bad[0].replace(',', ''))
    frame.to_csv('Steam.csv', encoding='utf-8', index=False)
    print(i, 'Done')
    i += 1
