class Bird():
    @classmethod
    def fly(cls):
        print("类方法fly", cls)

    @staticmethod
    def info(p):
        print("静态方法info", p)

Bird.fly()  # 类方法fly <class '__main__.Bird'>
Bird.info('crazyit')  #静态方法info crazyit

b = Bird()
b.fly()     # 类方法fly <class '__main__.Bird'>
b.info('fkit')  # 静态方法info fkit
