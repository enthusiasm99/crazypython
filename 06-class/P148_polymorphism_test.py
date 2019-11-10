#使用函数方法来实现多态性
def draw_pic(shape):
    print('--开始绘图--')
    shape.draw()

class Rectangle():
    def draw(self):
        print('绘制矩形')

class Triangle():
    def draw(self):
        print('绘制矩形')

class Circle():
    def draw(self):
        print('绘制矩形')


draw_pic(Rectangle()) 
draw_pic(Triangle())
draw_pic(Circle()) 