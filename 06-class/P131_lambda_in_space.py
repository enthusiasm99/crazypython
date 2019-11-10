global_fn = lambda p: print('执行lambda表达式， p参数', p)

class Category:
    cate_fn = lambda p: print('执行lambda表达式， p参数', p)

global_fn('fkit')

c = Category()
c.cate_fn()   # 类中的实例方法，第一个参数默认会绑定为self