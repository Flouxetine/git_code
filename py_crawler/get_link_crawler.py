import re
import urllib.request as request

def get_link(url):
    headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36")
    opener = request.build_opener()
    opener.addheaders = [headers]
    request.install_opener(opener)
    file = request.urlopen(url)
    data = str(file.read())
    pat = '(https?://[^\s";]+\.(\w|/)*)'
    link = re.compile(pat).findall(data)
    link = list(set(link))
    return link

url = "https://blog.csdn.net/"
link_list = get_link(url)
for link in link_list:
    print(link[0])