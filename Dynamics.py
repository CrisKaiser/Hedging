
import Global

class Dynamics:
    _equity = None
    _hedging_type = Global.OType.CALL
    _current_date = Global.START_DATE

    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity

    def run(self):
        pass
        #{
            #while(self.current_date <= Global.END_DATE):
                #equityUpdate()
                #self.current_date += 1
        #}
        
    def equityUpdate(self):
        self.updateHedgingType()
        self._equity.update(self._current_date, self._hedging_type)

    def sensitivityCheck(self):
        #{
            #-löse Portfolioposition auf nach bestimmten Kriterien
        #}
        pass

    def updateHedgingType(self):
        #{
            #-switch between Call and Put hedging depending on criteria
        #}
        self._hedging_type = Global.OType.CALL ###to be implemented