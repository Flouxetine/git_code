import urllib.request as request
import urllib.error as error

try:
    file = request.urlopen('http://blog.csdn.net')
    data = file.read()
    print(data)
except error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)
