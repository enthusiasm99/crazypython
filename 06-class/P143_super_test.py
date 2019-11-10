class Employee:
    def __init__(self, salary):
        self.salary = salary
    def work(self):
        print('普通员工的工资是：', self.salary)

class Customer:
    def __init__(self, favorite, address):
        self.favorite = favorite
        self.address = address
    def info(self):
        print('我是一个顾客，我的爱好是：%s, 地址是%s' % (self.favorite, self.address))

class Manager(Employee, Customer):
    def __init__(self, salary, favorite, address):
        print('--Manager 的构造方法--')
        #通过super()函数调用父类的构造方法
        super().__init__(salary)
        #与上一行代码效果相同
        #super(Manager, self).__init__(salary)
        Customer.__init__(self, favorite, address)

m = Manager(2500, 'IT产品', '广州')
m.work()
m.info()