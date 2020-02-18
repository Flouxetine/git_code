import urllib.request as request

url = 'https://blog.csdn.net/weiwei_pig/article/details/83577247'

reqe = request.Request(url)
reqe.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")

data = request.urlopen(reqe).read()
print(data)