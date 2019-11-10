s = 'crazyit.org is a good site'

print(s.startswith('crazyit'))

print(s.endswith('site'))

print(s.find('org'))

# 从索引9处开始查找，未找到，返回-1
print(s.find('org', 9))

print(s.index('org'))

#报错
# print(s.index('org',9))

print(s.replace('it', 'xxxx'))

# 创建翻译映射表
table = str.maketrans('crzy', '8888')
# 查找、替换
print(s.translate(table))

table2 = str.maketrans('crazy', '99999')
print(s.translate(table2))