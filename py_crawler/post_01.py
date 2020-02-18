import urllib.request as request

import urllib.parse as parse

url = 'https://www.iqianyue.com/mypost/'
postdata = parse.urlencode({
    'name':'zhangsan','pass':'aA123456'}).encode('utf-8')
req = request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
data = request.urlopen(req).read()
print(data)
