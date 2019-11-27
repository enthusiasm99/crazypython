class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)
    # 即定义的对象可以做 +=运算，但在 + 的左边
    def __iadd__(self, other):
        # 要求参与运算的另一个操作数必须是数值
        if not (isinstance(other, int) or isinstance(other, float)):
            raise TypeError('+=运算要求目标是数值')
        return Rectangle(self.width + other, self.height + other)
    def __repr__(self):
        return 'Rectangle(width = %g, height = %g)' % (self.width, self.height)
    
r = Rectangle(4, 5)
r += 2
print(r)