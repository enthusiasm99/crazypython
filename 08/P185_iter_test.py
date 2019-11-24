class Fibs:
    def __init__(self, len):
        self.first = 0
        self.sec = 1
        self.__len = len
    def __next__(self):
        if self.__len == 0:
            raise StopIteration
        self.first, self.sec = self.sec, self.first + self.sec
        self.__len -= 1
        return self.first
    def __iter__(self):
        return self
   # def __reversed__(self):


fibs = Fibs(10)
print(next(fibs))

for el in fibs:
    print(el, end = ' ')

fibs2 = list(reversed(fibs))
print(fibs2)


