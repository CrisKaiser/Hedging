
import numpy as np
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import Global
import matplotlib.pyplot as plt

class PhiView:

    _dynamics = None
    _phiCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _stockCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))

    def __init__(self, dynamics):
        if dynamics == None:
            raise ValueError("Dynamics is null")
        self._dynamics = dynamics
        self._dynamics.viewRegister(self)

    def updateView(self, date):
        _entry = DateCalc.daysBetweenDates(Global.START_DATE, date)
        self._phiCache[_entry] = self._dynamics._bigPhi
        self._stockCache[_entry] = Marketplace.getStockPriceOnDate(date)

    def draw(self):
        total_days = len(self._phiCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._phiCache, label="Phi", color='b')
        plt.title('Phi Chart')
        plt.xlabel('Date')
        plt.ylabel('Phi Value')
        step = total_days // 10 if total_days >= 10 else 1  
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def drawStockAndPhi(self):
        total_days = len(self._phiCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        fig, ax1 = plt.subplots(figsize=(10, 6))
        ax1.plot(dates, self._stockCache, label="Stock", color='g')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Stock Value', color='g')
        ax1.tick_params(axis='y', labelcolor='g')
        ax2 = ax1.twinx()
        ax2.plot(dates, self._phiCache, label="Phi", color='b')
        ax2.set_ylabel('Phi Value', color='b')
        ax2.tick_params(axis='y', labelcolor='b')
        plt.title('Phi and Stock Chart')
        step = total_days // 10 if total_days >= 10 else 1
        plt.xticks(dates[::step], rotation=45)
        ax1.grid(True)
        ax1.legend(["Stock"], loc='upper left')
        ax2.legend(["Phi"], loc='upper right')
        plt.tight_layout()
        plt.show()