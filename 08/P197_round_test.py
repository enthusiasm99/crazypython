class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

    def __round__(self, ndigits = 0):        
        self.width , self.height = round(self.width, ndigits), round(self.height, ndigits)
        return self
    def __repr__(self):
        return 'Rectangle(width = %g, height = %g)' % (self.width, self.height)
    
r = Rectangle(4.134, 5.567)
print(r)
result2 = round(r, 2)
print(result2)
result1 = round(r, 1)
print(result1)
print(dir(result1))
print(r.__dict__)
