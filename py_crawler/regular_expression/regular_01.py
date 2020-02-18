import re
# 普通字符作为原子
pattern = 'yue'
string = 'http://yum.iqianyue.com'
result_1 = re.search(pattern,string)
print(result_1)
# 非打印字符作为原子
pattern_1 = '\n'
string_1 = '''http://www.baidu.com
    http://yum.iqianyue.com'''
result_2 = re.search(pattern_1,string_1)
print(result_2)