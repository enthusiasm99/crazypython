def main():
    try:
        mtd(3)
    except Exception as e:
        print('程序出现异常：', e)    
    mtd(3)

def mtd(a):
    if a > 0 :
        raise ValueError('a的值大于0，不符合要求')

main()