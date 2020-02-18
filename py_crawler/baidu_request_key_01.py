import urllib.request as request
keyword = 'hello'
url = 'https://www.baidu.com/s?wd='+keyword
file = request.Request(url)
data = request.urlopen(file).read()
fhandle = open("D:/ren/mypython/web/3.html","wb")
fhandle.write(data)
fhandle.close()