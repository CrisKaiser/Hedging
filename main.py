
import Global
from Option import Option
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta

def main():

    start = "2016-10-20"
    now = "2016-10-20"
    end = "2016-10-27"

    stock_price = 600.174788539206
    
    oC = Option(start, now, end, stock_price, Global.OType.CALL)
    oP = Option(start, now, end, stock_price, Global.OType.PUT)
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

    d1 = HedgingDelta.calcNewDelta(oC)
    d2 = HedgingDelta.calcNewDelta(oP)

    print("Delta Call: " + str(d1))
    print("Delta Put: " + str(d2))

    

if __name__ == "__main__":
    main()