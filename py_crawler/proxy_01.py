def use_proxy(proxy_addr,url):
    import urllib.request as request
    proxy = request.ProxyHandler({'http':proxy_addr})
    opener = request.build_opener(proxy,request.HTTPHandler)
    request.install_opener(opener)
    data = request.urlopen(url).read().decode('utf-8')
    return data
proxy_addr = '202.75.210.45:7777'
date = use_proxy(proxy_addr ,'http://www.baidu.com')
print(len(date))