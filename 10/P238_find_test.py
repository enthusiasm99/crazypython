import re
# 忽略大小写
print(re.findall('fkit', 'FKIt is very goog, Fkit.org is my favorite', re.I))
it = re.finditer('fkit', 'FKIt is very goog, Fkit.org is my favorite', re.I)
for i in it:
    print(str(i.span()) + '---->' + i.group())