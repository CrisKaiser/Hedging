
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm

DECISION_MARGIN = 0.05

class DynamicsIV:
    _equity = None
    _current_date = Global.START_DATE
    _marketCache1 = np.zeros(Global.MARKET_CACHE_LENGTH1).tolist()
    _marketCache2 = np.zeros(Global.MARKET_CACHE_LENGTH2).tolist()
    _marketCache3 = np.zeros(Global.MARKET_CACHE_LENGTH3).tolist()
    _marketDataSet = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
    _marketDataSetForTripe = np.zeros(Global.TRIPEL_DATA_LENGTH).tolist()
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
        res = self.getPrediction(self._current_date)
        if res > 0.5 + DECISION_MARGIN:
            self._equity.hedge(self._current_date, Global.OType.CALL)
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)

    def fillMarketDataSet(self, current_date):
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketDataSet[i] = self.isStockIncreasing(new_date)

    def fillDataSetForTripe(self, current_date):
        for i in range(Global.TRIPEL_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketDataSetForTripe[i] = self.isStockIncreasing(new_date)

    def fillCaches(self, current_date):
        for i in range(Global.MARKET_CACHE_LENGTH1):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache1[i] = self.isStockIncreasing(new_date)
        for i in range(Global.MARKET_CACHE_LENGTH2):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache2[i] = self.isStockIncreasing(new_date)
        for i in range(Global.MARKET_CACHE_LENGTH3):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache3[i] = self.isStockIncreasing(new_date)

    def getSigmas(self, date):
        self.fillCaches(date)
        sigma1 = sum(self._marketCache1) / Global.MARKET_CACHE_LENGTH1
        sigma2 = sum(self._marketCache2) / Global.MARKET_CACHE_LENGTH2
        sigma3 = sum(self._marketCache3) / Global.MARKET_CACHE_LENGTH3
        res = [sigma1, sigma2, sigma3]
        return res / norm(res)

    def getPrediction(self, current_date):
        tripleArray = []
        for l1 in range(2,3):
            for l2 in range(5,8):
                for _l3_ in range(10, 30):
                    l3 = _l3_ #* 4 + 16
                    tripeSpecificArray = []
                    tripeSpecificArray.append([l1, l2, l3])
                    phiArray = self.getBigPhiArray(current_date, l1, l2, l3)
                    tripeSpecificArray.append(phiArray)
                    tripleArray.append(tripeSpecificArray)

        array = self.getBestMatchingTripleArray(tripleArray, current_date)

        predicton = array[1][0]
        print(array[0])
        print(predicton)
        return predicton

    def getBestMatchingTripleArray(self, dataSet, current_date):
        self.fillDataSetForTripe(current_date)

        _hitCache = np.zeros(len(dataSet))
        for i in range(len(dataSet)):
            _hitCount = 0
            for day in range(Global.TRIPEL_DATA_LENGTH):
                if dataSet[i][1][day] > 0.5 + DECISION_MARGIN and self._marketDataSetForTripe[day] == 1:
                    _hitCount += 1
                elif dataSet[i][1][day] < 0.5 +DECISION_MARGIN and self._marketDataSetForTripe[day] == 0:
                    _hitCache += 1
            _hitCache[i] = _hitCount
        
        max_index = np.argmax(_hitCache)
        return dataSet[max_index]


    def getBigPhiArray(self, current_date, l1, l2, l3):
        array = []
        for i in range(Global.TRIPEL_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)

            self.refreshCashLengths(l1, l2, l3, new_date)

            array.append(self.bigPhi(new_date))

        return array


    def bigPhi(self, current_date):
        self.fillMarketDataSet(self._current_date)
        matrix = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            matrix[i] = self.getSigmas(new_date)
        coVec = LinearRegression.calcSolutionVector(matrix, self._marketDataSet)
        currentSigma = self.getSigmas(current_date)
        sum = coVec[0] * currentSigma[0] + coVec[1] * currentSigma[1] + coVec[2] * currentSigma[2]
        self._bigPhi = sum
        self.notifyViews(current_date)
        return sum

    def refreshCashLengths(self, length1, length2, length3, current_date):
        Global.MARKET_CACHE_LENGTH1 = length1
        self._marketCache1 = np.zeros(Global.MARKET_CACHE_LENGTH1).tolist()

        Global.MARKET_CACHE_LENGTH2 = length2
        self._marketCache2 = np.zeros(Global.MARKET_CACHE_LENGTH2).tolist()

        Global.MARKET_CACHE_LENGTH3 = length3
        self._marketCache3 = np.zeros(Global.MARKET_CACHE_LENGTH3).tolist()

        self.fillCaches(current_date)

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if self._marketDictionary[current_date] > self._marketDictionary[_yesterday]:
            return 1
        else:
            return 0

    def preload(self):
        _date = DateCalc.getDateNDaysAfter(Global.START_DATE, -(1000) )
        while not DateCalc.areDatesEqual(_date, Global.END_DATE):
            self._marketDictionary[_date] = Marketplace.getStockPriceOnDate(_date)
            _date = DateCalc.getDateNDaysAfter(_date, 1)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
