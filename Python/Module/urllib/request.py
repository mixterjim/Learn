from urllib import request
for id in range(1000000000, 1000000010):
    url = "http://tieba.baidu.com/p/%d" % id
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    html = request.urlopen(req).read()
    file = open(str(id) + ".html", "wb")
    file.write(html)
    file.close()
