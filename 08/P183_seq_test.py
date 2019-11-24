def check_key(key):
    if not isinstance(key, int): raise TypeError("索引值必须是整数")
    if key < 0 : raise IndexError("索引值必须是非负整数")
    if key > 26 ** 3 : raise IndexError("索引值不能超过%d" % 26 ** 3)

class StringSeq:
    def __init__(self):
        self.__changed = {}
        self.__deleted = []
    def __len__(self):
        return 26 ** 3
    def __getitem__(self, key):
        check_key(key)
        if key in self.__changed:
            return self.__changed[key]
        if key in self.__deleted:
            return None
        three = key // (26 * 26)
        two = (key - three * 26 * 26) //26
        one = key % 26
        # chr() 用一个范围在 range(256)内的(就是0～255)整数作参数,返回当前整数对应的 ASCII 字符
        return chr(65 + three) + chr(65 + two) + chr(65 + one)
    def __setitem__(self, key, value):
        check_key(key)
        self.__changed[key] = value
    def __delitem__(self, key):
        check_key(key)
        if key not in self.__deleted: self.__deleted.append(key)
        if key in self.__changed: del self.__changed[key]
    # 自定义一个函数， 打印出删除的列表
    def print_del(self):
        print(self.__deleted)


    
sq = StringSeq()
print(len(sq))
print(sq[26 * 26])
print(sq[0])
print(sq[1])

sq[1] = 'fkit'
print(sq[1])

del sq[1]
print(sq[1])

sq[1] = 'crazyit'
print(sq[1])

del sq[2]
del sq[100]
sq.print_del()