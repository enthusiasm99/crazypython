class Dog:
    def jump(self):
        print("正在执行jump方法")
    def run(self):
        # 使用self参数引用调用run()方法的对象
        self.jump()
        print("正在执行run方法")

xiaobai = Dog()
xiaobai.run()