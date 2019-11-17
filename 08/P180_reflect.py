class Comment:
    def __init__(self, detail, view_time):
        self.detail = detail
        self.view_time = view_time
    def info():
        print("一条简单的评论，内容是%s" % self.detail)

c = Comment('疯狂Python讲义', 20)
print(hasattr(c, 'detail'))
print(hasattr(c, 'view_time'))
print(hasattr(c, 'info'))

print(getattr(c, 'detail'))
print(getattr(c, 'view_time'))
print(getattr(c, 'info', '默认值'))

setattr(c, 'detail', '天气不错')
setattr(c, 'view_time', 32)
print(c.detail, c.view_time)

setattr(c, 'test', '新增的测试属性')
print(c.test)

def bar():
    print('一个简单的bar方法')
setattr(c, 'info', bar)
c.info()