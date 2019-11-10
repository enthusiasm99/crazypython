class User:
    def __hide(self):
        print('示范隐藏的hide 方法')
    
    def getname(self):
        return self.__name
    def setname(self, name):
        if len(name) < 3 or len(name) > 8:
            raise ValueError('用户名长度必须在3-8之间')
        self.__name = name    
    name = property(getname, setname)

    def getage(self):
        return self.__age
    def setage(self, age):
        if age < 18 or age > 70:
            raise ValueError('用户年龄必须在18-70之间')
        self.__age = age
    age = property(getage, setage)

u = User()
#u.name = 'fk'     # ValueError: 用户名长度必须在3-8之间

u.name = 'fkit'
u.age = 23
print(u.name)
print(u.age)

u._User__hide()

u._User__name = 'fk'
print(u.name)