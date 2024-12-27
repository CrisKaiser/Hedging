
from Portfolio import Portfolio
from ClearingAccount import ClearingAccount

class Equity:

    portfolio = None
    clearingAcc = None

    def __init__(self):
        portfolio = Portfolio()
        clearingAcc = ClearingAccount()

    def getEquity(self, current_date):
        return portfolio.getValue(current_date) + clearingAcc.getBalance()

    def getPortfolio(self):
        return self.portfolio

    def getClearingAccount(self):
        return self.clearingAcc


