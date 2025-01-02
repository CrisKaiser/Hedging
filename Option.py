from framework.Marketplace import Marketplace

class Option:
    _creation_date = None
    _expire_date = None
    _K = None
    _optionType = None

    def __init__(self, creation_date, expire_date, K, optionType):
        self._creation_date = creation_date
        self._expire_date = expire_date
        self._K = K
        self._optionType = optionType

    def print(self, current_date):
        print("Option: " + str(self._creation_date) + " " + str(current_date) + " "+ str(self._expire_date) + " " + str(self._K) + " " + str(self._optionType) + " " + str( Marketplace.getStockPriceOnDate(current_date) ) + " " + str( Marketplace.get_yield_for_date(current_date) ))

    def get_creation_date(self):
        return self._creation_date

    def get_expire_date(self):
        return self._expire_date

    def getK(self):
        return self._K

    def getOptionType(self):
        return self._optionType

    def getMarketValue(self, current_date):
        return Marketplace.getMarketOptionPrice(self._creation_date, current_date, self._expire_date, self._K, self._optionType)
        
    def getMonteCarloValue(self, current_date):
        return Marketplace.getMonteCarloPrice(self._creation_date, current_date, self._expire_date, self._K, self._optionType)

    def getMonteCarloHedgingPricePairs(self, h, current_date):
        return Marketplace.getMonteCarloHedgingPricePairs(self._creation_date, current_date, self._expire_date, self._K, self._optionType, h)

    def getTheta(self, current_date):
        return Marketplace.getMarketOptionTheta(self._creation_date, current_date, self._expire_date, self._K, self._optionType)

    def getGamma(self, current_date):
        return Marketplace.getMarketOptionGamma(self._creation_date, current_date, self._expire_date, self._K, self._optionType)

    def getVega(self, current_date):
        return Marketplace.getMarketOptionVega(self._creation_date, current_date, self._expire_date, self._K, self._optionType)

    def getRho(self, current_date):
        return Marketplace.getMarketOptionRho(self._creation_date, current_date, self._expire_date, self._K, self._optionType)

    def getGreeks(self, current_date):
        return Marketplace.getMarketOptionGreeks(self._creation_date, current_date, self._expire_date, self._K, self._optionType)

    def getBigPhiA(self, current_date):
        return Marketplace.getOptionBigPhiA(self._creation_date, current_date, self._expire_date, self._K, self._optionType)

    