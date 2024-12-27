
class ClearingAccountView:

    _clearingAccount = None

    def __init__(self, clearingAccount):
        if clearingAccount == None:
            raise ValueError("ClearingAccount is null")
        self._clearingAccount = clearingAccount
        self._clearingAccount.viewRegister(self)

    def updateView(self):
        pass
