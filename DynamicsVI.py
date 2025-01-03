
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm


class DynamicsVI:
    _equity = None
    _current_date = Global.START_DATE
    _marketCache1 = np.zeros(Global.MARKET_CACHE1_LENGTH).tolist()
    _marketCache2 = np.zeros(Global.MARKET_CACHE2_LENGTH).tolist()
    _marketCache3 = np.zeros(Global.MARKET_CACHE3_LENGTH).tolist()
    _marketDataSet = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
    
    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def run(self):
        while(not DateCalc.areDatesEqual(self._current_date, Global.END_DATE)):
            self.equityUpdate()
            self._current_date = DateCalc.getDateNDaysAfter(self._current_date, 1)
        
    def equityUpdate(self):
        res = self.bigPi(self._current_date)
        if res > 0.75:
            self._equity.hedge(self._current_date, Global.OType.CALL)
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)

    def fillMarketDataSet(self, current_date):
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketDataSet[i] = self.isStockIncreasing(new_date)

    def fillCaches(self, current_date):
        for i in range(Global.MARKET_CACHE1_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache1[i] = self.isStockIncreasing(new_date)
        for i in range(Global.MARKET_CACHE2_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache2[i] = self.isStockIncreasing(new_date)
        for i in range(Global.MARKET_CACHE3_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache3[i] = self.isStockIncreasing(new_date)

    def getSigmas(self, date):
        self.fillCaches(date)
        sigma1 = sum(self._marketCache1) / Global.MARKET_CACHE1_LENGTH
        sigma2 = sum(self._marketCache2) / Global.MARKET_CACHE2_LENGTH
        sigma3 = sum(self._marketCache3) / Global.MARKET_CACHE3_LENGTH
        res = [sigma1, sigma2, sigma3]
        return res / norm(res)

    def bigPi(self, current_date):
        self.fillMarketDataSet(self._current_date)
        matrix = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            matrix[i] = self.getSigmas(new_date)
        coVec = LinearRegression.calcSolutionVector(matrix, self._marketDataSet)
        currentSigma = self.getSigmas(current_date)
        sum = coVec[0] * currentSigma[0] + coVec[1] * currentSigma[1] + coVec[2] * currentSigma[2]
        print(sum)
        return sum

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if Marketplace.getStockPriceOnDate(current_date) > Marketplace.getStockPriceOnDate(_yesterday):
            return 1
        else:
            return 0

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))
