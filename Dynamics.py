
import Global
from framework.DateCalc import DateCalc

class Dynamics:
    _equity = None
    _hedging_type = Global.OType.CALL
    _current_date = Global.START_DATE

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def run(self):
        while(not DateCalc.areDatesEqual(self._current_date, Global.END_DATE)):

            print(str(self._equity.getPortfolioValue(self._current_date)) + " " +  str(self._equity.getClearingAccountBalance()) + " "+ str(self._equity.getEquity(self._current_date)))
            self.equityUpdate()
            self._current_date = DateCalc.getDateNDaysAfter(self._current_date, 1)
           
        print("done")
        
    def equityUpdate(self):
        self.updateHedgingType()
        self._equity.update(self._current_date, self._hedging_type)

    def sensitivityCheck(self):
        #{
            #-löse Portfolioposition auf nach bestimmten Kriterien
        #}
        pass

    def updateHedgingType(self):
        #{
            #-switch between Call and Put hedging depending on criteria
        #}
        self._hedging_type = Global.OType.CALL ###to be implemented