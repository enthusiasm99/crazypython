'测试__all__变量的模块'

def hello():
    print('Hello, Python')
def world():
    print("Python world is funny")
def test():
    print('---test---')

__all__ = ['hello', 'world']