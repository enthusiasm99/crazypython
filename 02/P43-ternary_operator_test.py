a = 5
b = 3
st = 'a大于b' if  a > b  else 'a小于b'
print(st)


st = print('crazyit'), 'a大于b'  if  a > b  else 'a小于b'
print(st)


st = print('crazyit'); x = 20 if a>b else 'a不大于b'
print(st)
print(x)

c = 5
d = 5
print('c大于d' if c>d else ('c小于d' if c<d else 'c等于d'))
print('c大于d') if c>d else (print('c小于d') if c<d else print('c等于d'))