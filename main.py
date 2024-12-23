
import Global
from Option import Option
from framework.Marketplace import Marketplace

def main():

    start = "2016-10-20"
    now = "2016-10-20"
    end = "2016-10-27"
    
    oC = Option(start, now, end, 254.35399679951226, Global.OType.CALL)
    oP = Option(start, now, end, 254.35399679951226, Global.OType.PUT)
    p = oC.getMarketValue()
    p2 = oP.getMarketValue()
    s1 = Marketplace.get_yield_for_date(now)
    s2 = Marketplace.getHistoricalVolatility(now)
    s3 = Marketplace.getStockPriceOnDate(now)

    print("Option CALL Price: " + str(p))
    print("Option PUT Price: " + str(p2))
    print("Zins: " + str(s1))
    print("Vol: " + str(s2))
    print("StockPrice: " + str(s3))

if __name__ == "__main__":
    main()