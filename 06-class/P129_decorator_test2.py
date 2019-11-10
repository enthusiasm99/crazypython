def foo(fn):
    def bar(*args):
        print("===1===", args)
        n = args[0]
        print("===2===", n * (n-1))
        print(fn.__name__)
        fn(n * (n-1))
        print("*" * 20)
        return fn(n * (n-1))
    return bar

@foo
def my_test(a):
    print("==my_test 函数==", a)

print(my_test)

my_test(10)
my_test(6, 5)