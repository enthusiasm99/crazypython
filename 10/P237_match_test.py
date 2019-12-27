import re
m1 = re.match('www', 'www.fkit.ort') #从开始位置匹配
print(m1.span())
print(m1.group())
print(re.match('fkit', 'www.fkit.ort' ))  #从开头的位置匹配不到，返回NONE

m2 = re.search('www', 'www.fkit.ort')
print(m2.span())
print(m2.group())

m3 = re.search('fkit', 'www.fkit.ort')
print(m3.span())
print(m3.group())