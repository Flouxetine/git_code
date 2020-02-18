import urllib.request as request

url = 'http://yum.iqianyue.com'
for i in range(1,100):
    try:
        #设置请求超时时间request.urlopen("http://yum.iqianyue.com",timeout=30)
        file = request.urlopen("http://yum.iqianyue.com",timeout=30)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-----》"+str(e))