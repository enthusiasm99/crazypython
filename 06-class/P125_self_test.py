class User:
    def test(self):
        print("self参数", self)

u = User()
#  以方法形式调用test（）方法
u.test()         # self参数 <__main__.User object at 0x000000000290EE48>

# 将User对象的test方法赋值给foo变量
foo = u.test()
foo()            # self参数 <__main__.User object at 0x000000000290EE48>