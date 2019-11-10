def funA(fn):
    print('A')
    fn()
    return 'fkit'

@funA                 #相当于执行 funA(funB)
def funB():
    print('B')

print(funB)

'''
运行结果
A
B
fkit
'''