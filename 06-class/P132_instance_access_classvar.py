class Record:
    item = '鼠标'
    date = '2016-06-16'
    def info(self):
        print('info方法中：', self.item)
        print('info方法中：', self.date)

rc = Record()
print(rc.item)
print(rc.date)
rc.info()

Record.item = '键盘'
Record.date = '2016-08-18'
rc.info()
