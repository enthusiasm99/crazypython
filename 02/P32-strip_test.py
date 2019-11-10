s = '  this is a puppy   '
print(s)

# 删除左边的空白
print(s.lstrip())

# 删除右边的空白
print(s.rstrip())

# 删除两边的空白
print(s.strip())

# 看s是否有变化
print(s)

s2 = 'i think it is a scarecrow'
# 删除指定字符的功能
print(s2.lstrip('itow'))   #左边，则从'itow'中的i开始匹配，再向右逐步增加字母

print(s2.rstrip('itow'))   #左边，则从'itow'中的w开始匹配，再向左逐步增加字母。只删除最右边的 ow

print(s2.rstrip('row'))    #只删除最右边的 row， 最后一个单词中前面的r不会删除

print(s2.strip('itow'))    #两端匹配删除

