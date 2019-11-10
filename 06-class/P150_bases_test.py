class A:
    pass
class B:
    pass
class C(A, B):
    pass

print('A所有的父类:', A.__bases__)
print('B所有的父类', B.__bases__)
print('C所有的父类', C.__bases__)

print('A所有的子类', A.__subclasses__)
print('B所有的子类', B.__subclasses__)
print('C所有的子类', C.__subclasses__) 