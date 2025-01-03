
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import numpy as np

SM_SENS_UP = 3
SM_SENS_DOWN = -3

class StateMachine:
    def __init__(self):
        self.state = Global.StatesV.HEDGE_CALL
        self.counter = 0          

    def newLevel(self, equity, new_level):
        equity.updatePortfolioHedgingLevel(new_level)

    def transition(self, eq, level):
        if self.state == Global.StatesV.HEDGE_CALL:
            if self.counter == SM_SENS_UP:
                self.state = Global.StatesV.INVEST_CALL
            elif self.counter == SM_SENS_DOWN:
                self.state = Global.StatesV.HEDGE_PUT
        
        elif self.state == Global.StatesV.INVEST_CALL:
            if self.counter == 0:
                self.state = Global.StatesV.HEDGE_CALL
                self.newLevel(eq, level) 

        elif self.state == Global.StatesV.HEDGE_PUT:
            if self.counter == 0:
                self.state =  Global.StatesV.HEDGE_CALL

    def update_counter(self, value, eq, level):
        self.counter = value
        self.transition(eq, level)

class DynamicsV:
    _equity = None
    _current_date = Global.START_DATE
    _hedgingState = Global.StatesIV.WEAK_CALL
    _sm = StateMachine()
    _market_memory = [1,0,1,0,1,0,1,0,1,0]
    
    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def run(self):
        while(not DateCalc.areDatesEqual(self._current_date, Global.END_DATE)):
            self.updateState(self._current_date)
            self.equityUpdate()
            self._current_date = DateCalc.getDateNDaysAfter(self._current_date, 1)
        
    def equityUpdate(self):
        self.updateState(self._current_date)
        if self._sm.state == Global.StatesV.INVEST_CALL:
            self._equity.hedge(self._current_date, Global.OType.CALL)
            #print("INVESTING with CALLS")
        elif self._sm.state == Global.StatesV.HEDGE_CALL:
            self._equity.hedge(self._current_date, Global.OType.CALL)
            l = self._equity.portfolio._hedging_level 
            #print("HEDGING with CALLS at " + str(l))
        elif self._sm.state == Global.StatesV.HEDGE_PUT:
            self._equity.hedge(self._current_date, Global.OType.PUT)
            l = self._equity.portfolio._hedging_level 
            #print("HEDGING with PUTS " + str(l))

    def sensitivityCheck(self):
        #{
            #-löse Portfolioposition auf nach bestimmten Kriterien
        #}
        pass
            

    def updateState(self, current_date):
        _new_level = 1000 # self._equity.getEquity(self._current_date)
        self._market_memory.insert(0, 0)
        self._market_memory.pop()
        if self.isStockIncreasing(self._current_date):
            self._market_memory[0] = 1
        else:
            self._market_memory[0] = 0
        _value = None
        if sum(self._market_memory) < 7:
            _value = -3
        else:
            _value = 0
        self._sm.update_counter(_value, self._equity, _new_level)


    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if Marketplace.getStockPriceOnDate(current_date) > Marketplace.getStockPriceOnDate(_yesterday):
            return True
        else:
            return False

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))
