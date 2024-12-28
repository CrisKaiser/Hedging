import Global
import numpy as np
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import matplotlib.pyplot as plt

class EquityGreekView:
    _equity = None
    _thetaCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _vegaCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _gammaCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _rhoCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _valueCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _accCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))
    _wealthCache = np.zeros(DateCalc.daysBetweenDates(Global.START_DATE, Global.END_DATE))

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity
        self._equity.viewRegister(self)

    def updateView(self, date):
        _entry = DateCalc.daysBetweenDates(Global.START_DATE, date)
        self._thetaCache[_entry] = self._equity.getPortfolio().getPortfolioTheta(date)
        self._vegaCache[_entry] = self._equity.getPortfolio().getPortfolioVega(date)
        self._gammaCache[_entry] = self._equity.getPortfolio().getPortfolioGamma(date)
        self._rhoCache[_entry] = self._equity.getPortfolio().getPortfolioRho(date)
        self._valueCache[_entry] = self._equity.getPortfolio().getValue(date)
        self._accCache[_entry] = self._equity.getClearingAccountBalance()
        self._wealthCache[_entry] = self._equity.getEquity(date)

    def draw(self):
        total_days = len(self._thetaCache)
        dates = [DateCalc.getDateNDaysAfter(Global.START_DATE, i) for i in range(total_days)]
        plt.figure(figsize=(10, 6))
        plt.plot(dates, self._thetaCache, label="Theta", color='b')
        plt.plot(dates, self._wealthCache, label="Equity", color='r')
        plt.plot(dates, self._valueCache, label="Portfolio", color='k')
        plt.plot(dates, self._accCache, label="ClearingAccount", color='c')
        plt.title('Equity Greeks Chart')
        plt.xlabel('Date')
        plt.ylabel('Equity Greeks')
        step = total_days // 10 if total_days >= 10 else 1  
        plt.xticks(dates[::step], rotation=45)
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()