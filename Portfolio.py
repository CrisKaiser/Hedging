
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta
from Option import Option
import Global

class Portfolio:
    _delta = None
    _option = None

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
        if self._delta == None && self._option == None:
            return 0.0
        else:
            return _option.getMarketValue(current_date) + _delta * Marketplace.getStockPriceOnDate(current_date)

    def getValueDistribution(self, current_date):
        if self._delta == None && self._option == None:
            return 0.0
        else:
            return [_option.getMarketValue(current_date) , _delta * Marketplace.getStockPriceOnDate(current_date) ]

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

    def getPortfolioDelta(self):
        return self._delta

    def updateDelta(current_date):
        return HedgingDelta(self._option, current_date)
