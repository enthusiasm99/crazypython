s = 'crazyit.org is a good site'

# 使用空白进行分割
print(s.split())        #输出： ['crazyit.org', 'is', 'a', 'good', 'site']
print(s.split(None))    #同上

# 使用空白分割，最多只分割前2个单词
print(s.split(None, 2))  #输出： ['crazyit.org', 'is', 'a good site']

print(s.split('.'))     #输出： ['crazyit', 'org is a good site']



mylist = s.split()
# 使用 /  连接成字符串
print('/'.join(mylist))   #输出： crazyit.org/is/a/good/site
print(','.join(mylist))   #输出： crazyit.org,is,a,good,site
print('|'.join(mylist))   #输出： crazyit.org|is|a|good|site