class Inventory:
    item = '鼠标'
    quantity = 2000
    def change(self, item, quantity):
        self.item = item
        self.quantity = quantity

# 未改变类变量，只是定义了新的实例变量
iv = Inventory()
iv.change('显示器', 500)

print(iv.item)
print(iv.quantity)

print(Inventory.item)
print(Inventory.quantity)


# 修改类变量后，再查看实例变量
print('******修改类变量后，再查看实例变量******')
Inventory.item = '类变量item'
Inventory.quantity = '类变量quantity'

print(iv.item)
print(iv.quantity)


# 修改实例变量后，再查看类变量
print('*****修改实例变量后，再查看类变量*******')
iv.item = '实例变量item'
iv.quantity = '实例变量quantity'

print(Inventory.item)
print(Inventory.quantity)