
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm

DECISION_MARGIN = 0.05

class DynamicsIII:
    _equity = None
    _current_date = Global.START_DATE
    _marketDictionary = {}
    _marketCache = np.zeros(5)
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
        self.fillCache(self._current_date)
        if sum(self._marketCache) / 5.0 > 0.5 + DECISION_MARGIN:
            self._equity.hedge(self._current_date, Global.OType.CALL)
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)

    def fillCache(self, current_date):
        for i in range(5):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache[i] = self.isStockIncreasing(new_date)

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if self._marketDictionary[current_date] > self._marketDictionary[_yesterday]:
            return 1
        else:
            return 0

    def preload(self):
        _date = DateCalc.getDateNDaysAfter(Global.START_DATE, -(Global.MARKET_DATA_LENGTH + Global.MARKET_CACHE_LENGTH3) )
        while not DateCalc.areDatesEqual(_date, Global.END_DATE):
            self._marketDictionary[_date] = Marketplace.getStockPriceOnDate(_date)
            _date = DateCalc.getDateNDaysAfter(_date, 1)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
