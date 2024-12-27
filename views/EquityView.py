
class EquityView:

    _equity = None

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity
        self._equity.viewRegister(self)

    def updateView(self):
        pass
