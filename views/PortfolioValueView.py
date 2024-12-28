import Global
import numpy as np
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import matplotlib.pyplot as plt

class PortfolioValueView:

    _portfolio = None
    _valueCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))

    def __init__(self, portfolio):
        if  portfolio == None:
            raise ValueError("Portfolio is null")
        self. _portfolio = portfolio
        self._portfolio.viewRegister(self)

    def updateView(self, date):
        _entry = DateCalc.daysBetweenDates(Global.START_DATE, date)
        self._valueCache[_entry] = self._portfolio.getValue(date)

    def draw(self):
        total_days = len(self._valueCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._valueCache, label="Portfolio", color='b')
        plt.title('Portfolio Chart')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        step = total_days // 10 if total_days >= 10 else 1  
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

