import urllib.request as request
file = request.urlopen('http://www.baidu.com')
data = file.read()
data_line = file.readline()
print(data)
print(data_line)
#文件的两种写入方式
#1
#fhandle = open("D:/ren/mypython/web/1.html","wb")
#fhandle.write(data)
#fhandle.close()
#2
#request.urlretrieve("http://www.baidu.com","D:/ren/mypython/web/2.html")
#获取当前环境的相关信息
print(file.info())

print(file.getcode())

print(file.geturl())
#url地址的加解码
quote_handle = request.quote('http://www.sina.com.cn')
print(quote_handle)
unquote_handle = request.unquote('http%3A//www.sina.com.cn')
print(unquote_handle)
