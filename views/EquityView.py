
class EquityView:

    _equity = None

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def updateView(self):
        pass
