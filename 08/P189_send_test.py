def square_gen(val):
    i = 0
    out_val = None
    while True:
    # yield在中断时候，会把count往外返回 ，同时又变成一个接受外面指令的地址 ，完了赋值给了out_val
        out_val = (yield out_val ** 2) if out_val is not None else (yield i **2)
        if out_val is not None: print("======%d" % out_val)
        i += 1

sg = square_gen(5)
print(sg.send(None))
print(next(sg))
print('---------------')
print(sg.send(9))
print(next(sg))


# 参考： https://blog.csdn.net/u012164509/article/details/94436541
