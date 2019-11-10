class Dog:
    __slots__ = ('walk', 'age', 'name')
    def __init__(self, name):
        self.name = name
    def test():
        print('预告定义的test方法')

d = Dog('Snoopy')
from types import MethodType
d.walk = MethodType(lambda self: print('%s正在慢慢走' % self.name) , d)
d.age = 5
d.walk()
#d.foo = 30

#并不限制通过类方法来动态添加方法
Dog.bar = lambda self: print('并不限制通过类方法来添加')
d.bar()

#__slots__属性对子类是不起作用的
class GunDog(Dog):
    def __init__(self, name):
        super().__init__(name)
    pass

gd = GunDog('Puppy')
gd.speed = 90
print(gd.speed)