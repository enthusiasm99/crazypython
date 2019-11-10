#******************重写父类的方法
class Bird:
    def fly(self):
        print('我在天空里自由飞翔……')

class Ostrich(Bird):   #驼鸟
    #重写父类的方法
    def fly(self):
        print('我只能在地上奔跑')

o = Ostrich()
o.fly()

#******************调用父类的方法 **************
class BasicClass:
    def foo(self):
        print('父类中定义的foo方法')

class SubClass(BasicClass):
    def foo(self):
        print('子类重写父类中的foo方法')
    def bar(self):
        print('执行bar方法')
        self.foo()
        #调用父类的方法，注意括号中的self参数，即未绑定方法显式调用
        BasicClass.foo(self)

sc = SubClass()
sc.bar()

