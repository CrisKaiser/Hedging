
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta
from framework.DateCalc import DateCalc
from Option import Option
import Global

class Portfolio:
    _delta = None
    _option = None

    _views = []

    def rebuild(self, current_date, optionType):
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
            self.notifyViews(current_date)
            return revenue - invest

    def updateHedging(self, current_date, optionType):
        if self._option == None:
            pass
        else:
            print(self._option)
            st0 = str( self._option.getMarketValue(current_date) )
            st1 = str( self._delta )
            st2 = str( Marketplace.getStockPriceOnDate(current_date) )
            st3 = str( self.getValue(current_date) ) 
            print(st0 + " + " + st1 + " * " + st2 + " = " + st3)

        if self._option == None:
            self.rebuild(current_date, optionType)
        if DateCalc.isDateBefore(current_date, self._option.get_expire_date()):
            revenue = self.getValue(current_date)
            self.updateDelta(current_date)
            invest = self.getValue(current_date)
            return revenue - invest
        else:
            return self.rebuild(current_date, optionType)

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
