
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm

class DynamicsIII:
    _equity = None
    _current_date = Global.START_DATE

    #short-term
    _marketCache2 = np.zeros(2).tolist()
    _marketCache3 = np.zeros(3).tolist()

    #middle-term
    _marketCache6 = np.zeros(6).tolist()
    _marketCache7 = np.zeros(7).tolist()
    _marketCache8 = np.zeros(8).tolist()
    
    #long-term
    _marketCache16 = np.zeros(16).tolist()
    _marketCache17 = np.zeros(17).tolist()
    _marketCache18 = np.zeros(18).tolist()
    _marketCache19 = np.zeros(19).tolist()
    _marketCache20 = np.zeros(20).tolist()

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
        if res > 0.6:
            self._equity.hedge(self._current_date, Global.OType.CALL)
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)

    def fillMarketDataSet(self, current_date):
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketDataSet[i] = self.isStockIncreasing(new_date)

    def fillCaches(self, current_date):
        for i in range(2):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache2[i] = self.isStockIncreasing(new_date)
        for i in range(3):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache3[i] = self.isStockIncreasing(new_date)


        for i in range(6):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache6[i] = self.isStockIncreasing(new_date)
        for i in range(7):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache7[i] = self.isStockIncreasing(new_date)
        for i in range(8):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache8[i] = self.isStockIncreasing(new_date)


        for i in range(16):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache16[i] = self.isStockIncreasing(new_date)
        for i in range(17):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache17[i] = self.isStockIncreasing(new_date)
        for i in range(18):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache18[i] = self.isStockIncreasing(new_date)
        for i in range(19):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache19[i] = self.isStockIncreasing(new_date)
        for i in range(20):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache20[i] = self.isStockIncreasing(new_date)


    def getSigmas(self, date):
        self.fillCaches(date)
        sigma2 = sum(self._marketCache2) / 2
        sigma3 = sum(self._marketCache3) / 3

        sigma6 = sum(self._marketCache6) / 6
        sigma7 = sum(self._marketCache7) / 7
        sigma8 = sum(self._marketCache8) / 8

        sigma16 = sum(self._marketCache16) / 16
        sigma17 = sum(self._marketCache17) / 17
        sigma18 = sum(self._marketCache18) / 18
        sigma19 = sum(self._marketCache19) / 19
        sigma20 = sum(self._marketCache20) / 20

        res = [
            sigma2, sigma3, sigma6, sigma7, sigma8, sigma16, sigma17, sigma18, sigma19, sigma20
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
        _date = DateCalc.getDateNDaysAfter(Global.START_DATE, -(Global.MARKET_DATA_LENGTH + 100) )
        while not DateCalc.areDatesEqual(_date, Global.END_DATE):
            self._marketDictionary[_date] = Marketplace.getStockPriceOnDate(_date)
            _date = DateCalc.getDateNDaysAfter(_date, 1)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
