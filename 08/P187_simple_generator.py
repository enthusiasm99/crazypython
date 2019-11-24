def test(val, step):
    print('------函数开始执行------')
    cur = 0
    for i in range(val):
        cur += i * step
        yield cur 

t = test(10, 2)
print('========================')
print(next(t))
print(next(t))

for e in t:
    print(e, end = ' ')


t2 = test(10, 2)
print(list(t2))

t3 = test(10, 3)
print(tuple(t3))