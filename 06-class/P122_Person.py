class Person :
    '这是学习Python定义的一个Person类'
    # 下面定义了一个类变量
    hair = 'black'
    def __init__(self, name = 'Charlie', age =8):
        # 下面为Person对象增加两个实例变量
        self.name = name
        self.age = age
    # 下面定义了一个say方法
    def say(self, content):
        print(content)

p = Person()

print(p.name, p.age)   # Charlie 8
p.name = '李刚'
p.say('Python语言很简单，学习很容易！')   # Python语言很简单，学习很容易！
print(p.name, p.age)   # 李刚 8

# 动态增加实例变量
p.skills = ['programming', 'swimming']
print(p.skills)

#删除p对象的name实例变量
#del p.name
print(p.name)  # AttributeError: 'Person' object has no attribute 'name'

'''
动态增加对象方法
'''

# 先定义一个函数
def info(self):
    print('---info函数---', self)

# 对p的foo方法赋值（动态增加方法）
p.foo = info
# Python不会自动将调用者绑定到第一个参数
# 因此程序需要手动将调用者绑定到第一个参数
p.foo(p)

# 使用lambda表达式为p的bar方法赋值（动态增加方法）
p.bar = lambda self: print("---lambda表达式---", self)
p.bar(p)

'''
实现动态增加的方法自动绑定到第一个参数
'''

def intro_func(self, content):     #注意函数中的self参数
    print("我是一个人，信息为：%s" % content)

from types import MethodType
# 使用MethodType对intro_func进行包装，将该函数的第一个参数绑定为p
p.intro = MethodType(intro_func, p)
# 第一个参数已经绑定好了，无须传入
p.intro("生活在别处")

# 将以上函数改为lambda表达式
from types import MethodType
p.intro2 = MethodType(lambda self, content2: print("我还是一个人，信息为：%s" % content2), p)
p.intro2("单身狗啊单身狗")