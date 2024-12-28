
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta
from framework.DateCalc import DateCalc
from Option import Option
import Global

class Portfolio:
    _delta = None
    _option = None

    _views = []

    def update(self, current_date, optionType):
        if DateCalc.areDatesEqual(current_date, Global.START_DATE):
            _K = Marketplace.getStockPriceOnDate(current_date)
            _expire_date = DateCalc.getDateNDaysAfter(current_date, Global.MATURTIY)
            self._option = Option(current_date, _expire_date, _K, optionType)
            self.updateDelta(current_date)
            return 0.0
        elif DateCalc.isDateBefore(current_date, Global.END_DATE):
            revenue = self.getValue(current_date)
            _K = Marketplace.getStockPriceOnDate(current_date)
            _expire_date = DateCalc.getDateNDaysAfter(current_date, Global.MATURTIY)
            self._option = Option(current_date, _expire_date, _K, optionType)
            self.updateDelta(current_date)
            invest = self.getValue(current_date)
            self.notifyViews()
            return revenue - invest

    def getValue(self, current_date):
        if self._delta == None and self._option == None:
            return 0.0
        else:
            return self._option.getMarketValue(current_date) + abs(self._delta) * Marketplace.getStockPriceOnDate(current_date)

    def getValueDistribution(self, current_date):
        if self._delta == None and self._option == None:
            return 0.0
        else:
            return [self._option.getMarketValue(current_date) , self._delta * Marketplace.getStockPriceOnDate(current_date) ]

    def getPortfolioGamma(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return self._option.getGamma(current_date)

    def getPortfolioVega(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return self._option.getVega(current_date)

    def getPortfolioRho(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return self._option.getRho(current_date)

    def getPortfolioTheta(self, current_date):
        if self._option == None:
            raise ValueError("Option is None!")
        return self._option.getTheta(current_date)

    def getPortfolioDelta(self):
        return self._delta

    def updateDelta(self, current_date):
        self._delta = HedgingDelta.calcNewDelta(self._option, current_date)

    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self):
        for view in self._views:
            view.updateView()
