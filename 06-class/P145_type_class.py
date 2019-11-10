def fn(self):
    print('fn函数')

Dog = type('Dog', (object,), dict(walk=fn, age=6))
d = Dog()
print(type(d))
print(type(Dog))
d.walk()
print(Dog.age)