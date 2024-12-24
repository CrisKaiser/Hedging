
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta

class Portfolio:
    _delta = None
    _option = None


    def __init__(self, creation_date):
        pass

    def update(self, current_date):
        #{
            #1. Löse Portfoliopositon auf
            #2. Erwerbe neuen Optionsschein
            #3. 
        #}
        pass

    def getValue(self, current_date):
        return _option.getMarketValue(current_date) + _delta * Marketplace.getStockPriceOnDate(current_date)

    def getPortfolioGamma(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return _option.getGamma(current_date)

    def getPortfolioVega(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return _option.getVega(current_date)

    def getPortfolioRho(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return _option.getRho(current_date)

    def getPortfolioTheta(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return _option.getTheta(current_date)

    def updateDelta(current_date):
        return HedgingDelta(self._option, current_date)
