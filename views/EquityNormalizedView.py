
import numpy as np
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import Global
import matplotlib.pyplot as plt

class EquityNormalizedView:

    _equity = None
    _equityCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _stockCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _portfolioCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _clearAccCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    
    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity
        self._equity.viewRegister(self)

    def updateView(self, date):
        _entry = DateCalc.daysBetweenDates(Global.START_DATE, date)
        self._equityCache[_entry] = self._equity.getEquity(date)
        self._stockCache[_entry] = Marketplace.getStockPriceOnDate(date)
        self._clearAccCache[_entry] = self._equity.getClearingAccountBalance()
        self._portfolioCache[_entry] = self._equity.getPortfolio().getValue(date)
        
    def draw(self):
        multiplier = 1000.0 / self._equityCache[0]
        total_days = len(self._equityCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._equityCache * multiplier, label="Equity", color='b')
        plt.title('Equity Chart')
        plt.xlabel('Date')
        plt.ylabel('Equity Value')
        step = total_days // 10 if total_days >= 10 else 1  
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def drawSE(self):
        multiplierE = 1000.0 / self._equityCache[0]
        multiplierS = 1000.0 / self._stockCache[0]
        total_days = len(self._equityCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._equityCache * multiplierE, label="Equity", color='b')
        plt.plot(dates, self._stockCache * multiplierS, label="Stock", color='g') 
        plt.title('Equity and Stock Chart')
        plt.xlabel('Date')
        plt.ylabel('Value')
        step = total_days // 10 if total_days >= 10 else 1
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    def drawSED(self):
        multiplierE = 1000.0 / self._equityCache[0]
        multiplierS = 1000.0 / self._stockCache[0]
        total_days = len(self._equityCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._equityCache * multiplierE, label="Equity", color='b')
        plt.plot(dates, self._stockCache * multiplierS, label="Stock", color='g') 
        plt.plot(dates, self._portfolioCache * multiplierE, label="Portfolio", color='m') 
        plt.plot(dates, self._clearAccCache * multiplierE, label="Clearance Account", color='r') 
        plt.title('Equity, Stock and Distribution')
        plt.xlabel('Date')
        plt.ylabel('Value')
        step = total_days // 10 if total_days >= 10 else 1
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()


