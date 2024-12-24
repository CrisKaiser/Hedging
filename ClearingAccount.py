
from framework.Marketplace import Marketplace
import math 

class ClearingAccount:
    _balance = 0.0

    def withdraw(self, value):
        _balance -= value

    def deposit(self, value):
        _balance += value

    def getBalance(self):
        return _balance

    def interestUpdate(self, date):
        y = Marketplace.get_yield_for_date(date)
        #for daily update! Geomtric mean!#
        dYield = math.pow(1.0 + y, 1.0/365)
        _balance *= (1.0 + y/)    
