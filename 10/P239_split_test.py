import re
print(re.split(',', 'fkit, fkjava, crazyit'))
print(re.split(',', 'fkit, fkjava, crazyit', 1))
print(re.split('a', 'fkit, fkjava, crazyit'))     #输出  ['fkit, fkj', 'v', ', cr', 'zyit']
print(re.split('x', 'fkit, fkjava, crazyit')) 
