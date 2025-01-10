
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm

class DynamicsIII:
    _equity = None
    _current_date = Global.START_DATE

    _marketCache1 = np.zeros(1).tolist()
    _marketCache2 = np.zeros(2).tolist()
    _marketCache3 = np.zeros(3).tolist()
    _marketCache4 = np.zeros(4).tolist()
    _marketCache5 = np.zeros(5).tolist()
    _marketCache6 = np.zeros(6).tolist()
    _marketCache7 = np.zeros(7).tolist()
    _marketCache8 = np.zeros(8).tolist()
    _marketCache9 = np.zeros(9).tolist()
    _marketCache10 = np.zeros(10).tolist()

    _marketDataSet = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
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
        res = self.bigPi(self._current_date)
        if res > 0.0:
            self._equity.hedge(self._current_date, Global.OType.CALL)
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)

    def fillMarketDataSet(self, current_date):
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketDataSet[i] = self.isStockIncreasing(new_date)

    def fillCaches(self, current_date):
        for i in range(1):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache1[i] = self.isStockIncreasing(new_date)
        for i in range(2):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache2[i] = self.isStockIncreasing(new_date)
        for i in range(3):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache3[i] = self.isStockIncreasing(new_date)
        for i in range(4):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache4[i] = self.isStockIncreasing(new_date)
        for i in range(5):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache5[i] = self.isStockIncreasing(new_date)
        for i in range(6):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache6[i] = self.isStockIncreasing(new_date)
        for i in range(7):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache7[i] = self.isStockIncreasing(new_date)
        for i in range(8):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache8[i] = self.isStockIncreasing(new_date)
        for i in range(9):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache9[i] = self.isStockIncreasing(new_date)
        for i in range(10):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache10[i] = self.isStockIncreasing(new_date)

    def getSigmas(self, date):
        self.fillCaches(date)
        sigma1 = sum(self._marketCache1) / 1
        sigma2 = sum(self._marketCache2) / 2
        sigma3 = sum(self._marketCache3) / 3
        sigma4 = sum(self._marketCache4) / 4
        sigma5 = sum(self._marketCache5) / 5
        sigma6 = sum(self._marketCache6) / 6
        sigma7 = sum(self._marketCache7) / 7
        sigma8 = sum(self._marketCache8) / 8
        sigma9 = sum(self._marketCache9) / 9
        sigma10 = sum(self._marketCache10) / 10

        res = [
            sigma1, sigma2, sigma3, sigma4, sigma5, sigma6, sigma7, sigma8, sigma9, sigma10
        ]
        return res / norm(res)

    def bigPi(self, current_date):
        self.fillMarketDataSet(self._current_date)
        print(self._marketDataSet)
        matrix = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            matrix[i] = self.getSigmas(new_date)
        coVec = LinearRegression.calcSolutionVector(matrix, self._marketDataSet)
        print(coVec)
        currentSigma = self.getSigmas(current_date)
        sum = 0
        for i in range(10):
            sum += coVec[i] * currentSigma[i]
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
        _date = DateCalc.getDateNDaysAfter(Global.START_DATE, -(Global.MARKET_DATA_LENGTH + 10) )
        while not DateCalc.areDatesEqual(_date, Global.END_DATE):
            self._marketDictionary[_date] = Marketplace.getStockPriceOnDate(_date)
            _date = DateCalc.getDateNDaysAfter(_date, 1)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
