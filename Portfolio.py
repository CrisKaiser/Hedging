
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta
from Option import Option
import Global

class Portfolio:
    _delta = None
    _option = None

    def __init__(self):
        self.setUpPortfolio()

    def setUpPortfolio(self):
        _expire_date = None #to be implemented: = GLobal.Start_date + 2days 
        _K = Marketplace.getStockPriceOnDate(Global.START_DATE)
        self._option = Option(Global.START_DATE, _expire_date, _K, Global.OType.CALL) #Call as default
        self._delta = HedgingDelta(self._option, Global.START_DATE)

    def update(self, current_date, optionType):
        revenue = self.getValue()
        #{
            #(1. Löse Portfoliopositon auf)
            #2. Erwerbe neuen Optionsschein mit K = ST, T = t+2
            #3. 
        #}
        invest = self.getValue()
        return revenue - invest

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
