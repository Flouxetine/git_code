import urllib.request as req
url = 'http://www.httpbin.org/'
date = req.urlopen(url)
print(type(date))
print(date.getcode())



