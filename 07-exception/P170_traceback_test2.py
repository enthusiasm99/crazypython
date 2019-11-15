import traceback
class SelfException(Exception): pass

def main():
    firestMethod()
def firestMethod():
    secondMethod()
def secondMethod():
    thirdMethod()
def thirdMethod():
    raise Exception("自定义异常信息！")

try:
    main()
except:
    traceback.print_exc()
    traceback.print_exc(file = open('log.txt', 'a'))
