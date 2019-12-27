import re

def fun(matched):
    value = '《疯狂' + (matched.group('lang')) + '讲义》'
    return value

s  = 'Python 很好， Kotlin也很好'
print(re.sub(r'(?P<lang>\w+)', fun, s, flags = re.A))