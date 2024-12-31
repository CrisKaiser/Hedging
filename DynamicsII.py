
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace

class DynamicsII:
    _equity = None
    _hedging_type = None #Global.OType.CALL
    _current_date = Global.START_DATE
    _hedgingState = Global.StatesII.CALL

    _hitCount = 0

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def run(self):
        while(not DateCalc.areDatesEqual(self._current_date, Global.END_DATE)):
            if (self.isStockIncreasing(self._current_date) and self._hedging_type == Global.OType.CALL) or (not self.isStockIncreasing(self._current_date) and self._hedging_type == Global.OType.PUT):
                self._hitCount += 1
            self.updateState(self._current_date)
            self.updateHedgingType()
            self.equityUpdate()
            self._current_date = DateCalc.getDateNDaysAfter(self._current_date, 1)
           
        print("hit count: " + str(self._hitCount))
        
    def equityUpdate(self):
        self.updateHedgingType()
        self._equity.hedge(self._current_date, self._hedging_type)

    def sensitivityCheck(self):
        #{
            #-löse Portfolioposition auf nach bestimmten Kriterien
        #}
        pass

    def updateHedgingType(self):
        if self._hedgingState == Global.StatesII.CALL:
            self._hedging_type = Global.OType.CALL
        else:
            self._hedging_type = Global.OType.CALL

    def updateState(self, current_date):
        if self.isStockIncreasing(current_date):
            self._hedgingState = Global.StatesII.CALL
        else:
            self._hedgingState = Global.StatesII.CALL

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if Marketplace.getStockPriceOnDate(current_date) > Marketplace.getStockPriceOnDate(_yesterday):
            return True
        else:
            return False

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))
