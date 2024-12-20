import Marketplace

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

    def get_creation_date(self):
        return self._creation_date

    def get_expire_date(self):
        return self._expire_date

    def getK(self):
        return self._K

    def getOptionType(self):
        return self._optionType

    def getValue(self):
        return Marketplace.getMarketOptionPrice(self._creation_date, self._current_date, self._expire_date, self._K, self._optionType)

    def getTheta(self):
        return Marketplace.getMarketOptionTheta(self._creation_date, self._current_date, self._expire_date, self._K, self._optionType)

    def getGamma(self):
        return Marketplace.getMarketOptionGamma(self._creation_date, self._current_date, self._expire_date, self._K, self._optionType)

    def getVega(self):
        return Marketplace.getMarketOptionVega(self._creation_date, self._current_date, self._expire_date, self._K, self._optionType)

    def getRho(self):
        return Marketplace.getMarketOptionRho(self._creation_date, self._current_date, self._expire_date, self._K, self._optionType)

    def getGreeks(self):
        return Marketplace.getMarketOptionGreeks(self._creation_date, self._current_date, self._expire_date, self._K, self._optionType)


    