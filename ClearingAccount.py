
from framework.Marketplace import Marketplace
import math 

class ClearingAccount:
    _balance = 0.0
    _views = []

    def updateBalance(self, value):
        self._balance += value

    def getBalance(self):
        return self._balance

    def interestUpdate(self, date):
        y = Marketplace.get_yield_for_date(date)
        #for daily update! Geomtric mean!#
        dYield = math.pow(1.0 + y, 1.0/365)
        self._balance *= dYield    
        self.notifyViews()

    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self):
        for view in self._views:
            view.updateView()

