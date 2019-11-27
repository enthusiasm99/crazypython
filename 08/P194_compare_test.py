class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)
    # 能比较大，则能比较小
    def __gt__(self, other):
        # 要求参与运算的另一个操作数必须是Rectangle类
        if not isinstance(other, Rectangle):
            raise TypeError('+运算要求目标是Rectangle类')
        return True if self.width * self.height > other.width * other.height else False

    # 能比较相等，则能比较不相等
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError('+运算要求目标是Rectangle类')
        return True if self.width * self.height == other.width * other.height else False

    # 能比较大于等于 ，则能比较小于等于
    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError('+运算要求目标是Rectangle类')
        return True if self.width * self.height >= other.width * other.height else False    
    def __repr__(self):
        return 'Rectangle(width = %g, height = %g)' % (self.width, self.height)

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 4)
print(r1 > r2)
print(r1 >= r2)
print(r1 < r2)
print(r1 == r2)
print(r1 != r2)
print(r1)
