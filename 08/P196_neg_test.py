class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

    def __neg__(self):        
        self.width , self.height = self.height, self.width
    def __repr__(self):
        return 'Rectangle(width = %g, height = %g)' % (self.width, self.height)
    
r = Rectangle(4, 5)
print(r)
-r
print(r)
