class AuctionException(Exception): pass
class AuctionTest:
    def __init__(self, init_price):
        self.init_price = init_price
    def bid(self, bid_price):
        d = 0.0
        try:
            d = float(bid_price)
        except Exception as e:
            print("转换出现异常：", e)
            raise 
        if self.init_price > d:
            raise AuctionException("竞拍价比起拍价低，不允许竞拍！")
        initPrice = d
        print("最新的竞价是：", initPrice)

def main():
    at = AuctionTest(20.4)
    try:
        at.bid("ggg")
    except Exception as ae:
        print("main函数捕获的异常:",  type(ae))

main()