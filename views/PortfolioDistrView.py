
class PortfolioDistrView:

    _portfolio = None

    def __init__(self, portfolio):
        if  _portfolio == None:
            raise ValueError("Portfolio is null")
        self. _portfolio = portfolio
        self._portfolio.viewRegister(self)
        
    def updateView(self):
        pass