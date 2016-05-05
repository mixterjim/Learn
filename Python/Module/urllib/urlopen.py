from urllib import request
for id in range(1000000000, 1000000010):
    url = "http://tieba.baidu.com/p/%d" % id
    html = request.urlopen(url).read()
    file = open(str(id) + ".html", "wb")
    file.write(html)
    file.close()
