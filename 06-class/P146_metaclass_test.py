class ItemMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['cal_price'] = lambda self: self.price * self.discount
        return type.__new__(cls, name, bases, attrs)

class Book(metaclass=ItemMetaClass):
    __slots__ = ('name', 'price', '_discount')
    def __init__(self, name, price):
        self.name = name
        self.price = price    
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount

class CellPhone(metaclass=ItemMetaClass):
    __slots__ = ('price', '_discount')
    def __init__(self, price):
        self.price = price
    @property
    def discount(self):
        return self._discount
    @discount.setter
    def discount(self, discount):
        self._discount = discount

b = Book('Python疯狂讲义', 89)
b.discount = 0.76
print(b.cal_price())

c = CellPhone(2399)
c.discount = 0.85
print(c.cal_price())

