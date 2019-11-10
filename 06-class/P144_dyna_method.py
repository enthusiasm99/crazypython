class Cat:
    def __init__(self, name):
        self.name = name

def walk_func(self):
    print('%s慢慢地走过一片草地' % self.name)

d1 = Cat('Garfield')
d2 = Cat('Kitty')

Cat.walk = walk_func
d1.walk()
d2.walk()

