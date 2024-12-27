
class Dynamics:
    
    _equity = None

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def run(self):
        pass
        
    def portfolioUpdate(self):
        #{
            #-neuen Portfoliostand setzen
        #}

    def sensitivityCheck(self):
        #{
            #-löse Portfolioposition auf nach bestimmten Kriterien
        #}