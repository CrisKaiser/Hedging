
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm

class DynamicsI:
    _equity = None
    _current_date = Global.START_DATE
    _marketDictionary = {}
    _views = []
    _bigPhi = None
    
    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity
        self.preload()
        print("Market Data loaded")

    def run(self):
        while(not DateCalc.areDatesEqual(self._current_date, Global.END_DATE)):
            self.equityUpdate()
            self._current_date = DateCalc.getDateNDaysAfter(self._current_date, 1)
            if self._current_date == Global.END_DATE:
                print(self._equity.getEquity(self._current_date))

    def equityUpdate(self):
        if self.isStockIncreasing(self._current_date) == 1:
            self._equity.hedge(self._current_date, Global.OType.CALL)
            self._bigPhi = 1
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)
            self._bigPhi = 0
        self.notifyViews(self._current_date)

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if self._marketDictionary[current_date] > self._marketDictionary[_yesterday]:
            return 1
        else:
            return 0

    def preload(self):
        _date = DateCalc.getDateNDaysAfter(Global.START_DATE, -(Global.MARKET_DATA_LENGTH + 1000) )
        while not DateCalc.areDatesEqual(_date, Global.END_DATE):
            self._marketDictionary[_date] = Marketplace.getStockPriceOnDate(_date)
            _date = DateCalc.getDateNDaysAfter(_date, 1)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
