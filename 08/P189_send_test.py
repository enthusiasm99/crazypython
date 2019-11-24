def square_gen(val):
    i = 0
    out_val = None
    while True:
        out_val = (yield out_val ** 2) if out_val is not None else (yield i **2)
        if out_val is not None: print("======%d" % out_val)
        i += 1

sg = square_gen(5)
print(sg.send(None))
print(next(sg))
print('---------------')
print(sg.send(9))
print(next(sg))

