import os
def test():
    fis = None
    try:
        fis = open(a.txt)
    except OSError as e:
        print(e.strerror)
        return
        #os._exit(1)
    finally:
        if fis is not None:
            try:
                fis.close()
            except OSError as ios:
                print(ios.strerror)
        print(' 执行finally块里的资源回收！')
test()