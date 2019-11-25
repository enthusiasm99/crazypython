def square_gen():
    i = 0
    sen_val = None
    while True:
        sen_val = (yield sen_val ** 2) if sen_val is not None else (yield i **2)
        if sen_val is not None: print("======%d" % sen_val)
        i += 1

sg = square_gen()
print(sg.send(None))
print(next(sg))
print('---------------')
print(sg.send(8))
print(next(sg))
