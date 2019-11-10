def auth(fn):
    def auth_fn(*args):
        print("-----模拟执行权限检查-----")
        fn(*args)
    return auth_fn

@auth
def test(a, b):
    print("执行test函数，参数a: %s, 参数b: %s"  %  (a, b))

test(20, 15)

'''运行结果
-----模拟执行权限检查-----
执行test函数，参数a: 20, 参数b: 15
'''