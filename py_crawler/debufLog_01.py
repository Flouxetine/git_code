# 有时候我们希望在程序运行的过程中，边运行边打印调试日志，此时我们需要开启DebugLog
# 1）需要在urllib.request.HTTPHandler()和urllib.request.HTTPSHandler()将debuglevel设置为1
import urllib.request as request
httphd = request.HTTPHandler(debuglevel=1)
httpshd = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(httphd,httpshd)
request.install_opener(opener)
data = request.urlopen('http://edu.51cto.com')