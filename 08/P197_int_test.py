class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

    def __int__(self):        
        return int(self.width * self.height )
    def __repr__(self):
        return 'Rectangle(width = %g, height = %g)' % (self.width, self.height)
    
r = Rectangle(4.5, 5.7)
print(r)
print(int(r))
