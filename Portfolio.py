
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta
from framework.DateCalc import DateCalc
from Option import Option
import Global

class Portfolio:
    _delta = None
    _option = None
    _hedging_unit = None
    _views = []

    def rebuild(self, current_date, optionType):
        if DateCalc.areDatesEqual(current_date, Global.START_DATE):
            _K = Marketplace.getStockPriceOnDate(current_date)
            _expire_date = DateCalc.getDateNDaysAfter(current_date, Global.MATURTIY)
            self._option = Option(current_date, _expire_date, _K, optionType)
            self.updateDelta(current_date)
            self.updateHedgingUnit(current_date)
            return 0.0
        elif DateCalc.isDateBefore(current_date, Global.END_DATE):
            revenue = self.getValue(current_date)
            _K = Marketplace.getStockPriceOnDate(current_date)
            _expire_date = DateCalc.getDateNDaysAfter(current_date, Global.MATURTIY)
            self._option = Option(current_date, _expire_date, _K, optionType)
            self.updateDelta(current_date)
            if not Global.DYNAMIC_INVEST:
                self.updateHedgingUnit(current_date)
            invest = self.getValue(current_date)
            self.notifyViews(current_date)
            return revenue - invest

    def updateHedgingLevel(self, new_level):
        self._hedging_level = new_level

    def updateHedging(self, current_date, optionType):
        if self._option == None:
            return self.rebuild(current_date, optionType)
        if self._option._optionType != optionType:
            return self.rebuild(current_date, optionType)
        if DateCalc.isDateBefore(current_date, self._option.get_expire_date()):
            revenue = self.getValue(current_date)
            self.updateDelta(current_date)
            invest = self.getValue(current_date)
            return revenue - invest
        else:
            return self.rebuild(current_date, optionType)

    def updateHedgingUnit(self, current_date):
        if self._delta == None or self._option == None:
            raise ValueError("Null not allowed")
        else:
            self._hedging_unit = Global.INITIAL_INVEST / (self._option.getMarketValue(current_date) + abs(self._delta) * Marketplace.getStockPriceOnDate(current_date))

    def getValue(self, current_date):
        if self._delta == None or self._option == None:
            return 0.0
        else:
            return self._hedging_unit * (self._option.getMarketValue(current_date) + abs(self._delta) * Marketplace.getStockPriceOnDate(current_date))

    def getValueDistribution(self, current_date):
        if self._delta == None and self._option == None:
            return 0.0
        else:
            self._option.print(current_date)
            return  [self._hedging_unit * self._option.getMarketValue(current_date) , self._hedging_unit * self._delta * Marketplace.getStockPriceOnDate(current_date) ]

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

    def getPortfolioDelta(self, current_date):
        if self._option == None:
            return 0.0
        return HedgingDelta.calcNewDelta(self._option, current_date)

    def updateDelta(self, current_date):
        self._delta = HedgingDelta.calcNewDelta(self._option, current_date)

    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
