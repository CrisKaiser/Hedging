
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm

class Dynamics:
    _equity = None
    _current_date = Global.START_DATE
    _marketCache1 = np.zeros(5).tolist()
    _marketCache2 = np.zeros(10).tolist()
    _marketCache3 = np.zeros(20).tolist()
    _marketDataSet = [0]
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
        
    def equityUpdate(self):
        res = self.bigPi(self._current_date)
        if res > 0.6:
            self._equity.hedge(self._current_date, Global.OType.CALL)
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)

    def fillMarketDataSet(self, current_date):
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketDataSet[i] = self.isStockIncreasing(new_date)

    def fillCaches(self, current_date):
        for i in range(5):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache1[i] = self.isStockIncreasing(new_date)
        for i in range(10):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache2[i] = self.isStockIncreasing(new_date)
        for i in range(20):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache3[i] = self.isStockIncreasing(new_date)

    def getSigmas(self, date):
        self.fillCaches(date)
        sigma1 = sum(self._marketCache1) / 5
        sigma2 = sum(self._marketCache2) / 10
        sigma3 = sum(self._marketCache3) / 20
        res = [sigma1, sigma2, sigma3]

        return res / norm(res)

    def bigPi(self, current_date):
        self.fillMarketDataSet(self._current_date)
        matrix = [0]
        matrix[0] = self.getSigmas(current_date)
        coVec = LinearRegression.calcSolutionVector(matrix, self._marketDataSet)
        currentSigma = self.getSigmas(current_date)
        sum = coVec[0] * currentSigma[0] + coVec[1] * currentSigma[1] + coVec[2] * currentSigma[2]
        self._bigPhi = sum
        self.notifyViews(current_date)
        print(current_date)
        return sum

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if self._marketDictionary[current_date] > self._marketDictionary[_yesterday]:
            return 1
        else:
            return 0

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    def preload(self):
        _date = DateCalc.getDateNDaysAfter(Global.START_DATE, -(21) )
        while not DateCalc.areDatesEqual(_date, Global.END_DATE):
            self._marketDictionary[_date] = Marketplace.getStockPriceOnDate(_date)
            _date = DateCalc.getDateNDaysAfter(_date, 1)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
