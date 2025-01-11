
from Portfolio import Portfolio
from ClearingAccount import ClearingAccount
from framework.DateCalc import DateCalc
import Global
import csv

class Equity:
    portfolio = None
    clearingAcc = None
    equity_data = []
    _views = []

    def __init__(self):
        self.portfolio = Portfolio()
        self.clearingAcc = ClearingAccount()

    def rebuild(self, current_date, optionType):
        _revenue = self.portfolio.rebuild(current_date, optionType)
        self.clearingAcc.updateBalance(_revenue)
        self.clearingAcc.interestUpdate(current_date)
        self.notifyViews(current_date)

    def hedge(self, current_date, optionType):
        _revenue = self.portfolio.updateHedging(current_date, optionType)
        self.clearingAcc.updateBalance(_revenue)
        self.clearingAcc.interestUpdate(current_date)
        self.notifyViews(current_date)

    def getEquity(self, current_date):
        return self.portfolio.getValue(current_date) + self.clearingAcc.getBalance()

    def getPortfolio(self):
        return self.portfolio

    def getClearingAccount(self):
        return self.clearingAcc

    def getClearingAccountBalance(self):
        return self.clearingAcc.getBalance()

    def getPortfolioDelta(self):
        return self.portfolio.getPortfolioDelta()
        
    def getPortfolioValue(self, current_date):
        return self.portfolio.getValue(current_date)

    def getPortfolioValueDistribution(self, current_date):
        return self.portfolio.getValueDistribution(current_date) #[value option, value asset]

    def updatePortfolioHedgingLevel(self, new_level):
        self.portfolio.updateHedgingLevel(new_level)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)

        equity_value = self.getEquity(current_date)
        self.equity_data.append([current_date, equity_value])
        
        if DateCalc.areDatesEqual(current_date, DateCalc.getDateNDaysAfter(Global.END_DATE, -1)):
            with open('equity_data.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Date', 'Equity'])
                writer.writerows(self.equity_data)

        
