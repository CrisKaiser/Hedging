
import numpy as np
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import Global
import matplotlib.pyplot as plt

class EquityView:

    _equity = None
    _equityCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _stockCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity
        self._equity.viewRegister(self)

    def updateView(self, date):
        _entry = DateCalc.daysBetweenDates(Global.START_DATE, date)
        self._equityCache[_entry] = self._equity.getEquity(date)
        self._stockCache[_entry] = Marketplace.getStockPriceOnDate(date)

    def draw(self):
        total_days = len(self._equityCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._equityCache, label="Equity", color='b')
        plt.title('Equity Chart')
        plt.xlabel('Date')
        plt.ylabel('Equity Value')
        step = total_days // 10 if total_days >= 10 else 1  
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def drawStockAndEquity(self):
        total_days = len(self._equityCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._equityCache, label="Equity", color='b')
        plt.plot(dates, self._stockCache, label="Stock", color='g') 
        plt.title('Equity and Stock Chart')
        plt.xlabel('Date')
        plt.ylabel('Value')
        step = total_days // 10 if total_days >= 10 else 1
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    
