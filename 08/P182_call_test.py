class User:
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd
    def validLogin(self):
        print('验证%s的登录' % self.name)

u = User('crazyit', 'leegang')
print(hasattr(u.name, '__call__'))
print(hasattr(u.passwd, '__call__'))
print(hasattr(u.validLogin, '__call__'))

