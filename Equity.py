
from Portfolio import Portfolio
from ClearingAccount import ClearingAccount

class Equity:
    portfolio = None
    clearingAcc = None

    def __init__(self):
        portfolio = Portfolio()
        clearingAcc = ClearingAccount()

    def update(self, current_date, optionType):
        _revenue = self.portfolio.update(current_date, optionType)
        self.clearingAcc.updateBalance(_revenue)
        self.clearingAcc.interestUpdate(current_date)

    def getEquity(self, current_date):
        return portfolio.getValue(current_date) + clearingAcc.getBalance()

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
    


