
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace

class DynamicsIV:
    _equity = None
    _hedging_type = None #Global.OType.CALL
    _current_date = Global.START_DATE
    _hedgingState = Global.StatesIV.WEAK_CALL

    _hitCount = 0

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def run(self):
        while(not DateCalc.areDatesEqual(self._current_date, Global.END_DATE)):
            self.updateState(self._current_date)
            self.updateHedgingType()
            self.equityUpdate()
            self._current_date = DateCalc.getDateNDaysAfter(self._current_date, 1)
        
    def equityUpdate(self):
        self.updateHedgingType()
        self._equity.hedge(self._current_date, self._hedging_type)

    def sensitivityCheck(self):
        #{
            #-löse Portfolioposition auf nach bestimmten Kriterien
        #}
        pass

    def updateHedgingType(self):
        if self.isStockIncreasing(self._current_date):
            self._hedging_type = Global.OType.CALL
        else:
            self._hedging_type = Global.OType.PUT

    def updateState(self, current_date):
        if self.isStockIncreasing(current_date):
            newStateValue = self.clamp((self._hedgingState.value + 1), 0, 2)
            self._hedgingState = Global.StatesIV(newStateValue)
        else:
            newStateValue = self.clamp((self._hedgingState.value - 1), 0, 2)
            self._hedgingState = Global.StatesIV(newStateValue)

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if Marketplace.getStockPriceOnDate(current_date) > Marketplace.getStockPriceOnDate(_yesterday):
            return True
        else:
            return False

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))
