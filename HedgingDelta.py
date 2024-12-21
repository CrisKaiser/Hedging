
import Global

class HedgingDelta:

    def __init__(self):
        pass

    def calcNewDelta(self):
        if Global.HEDGING_MODE == 0:
            #Black-Scholes
        elif Global.HEDGING_MODE == 1:
            #Monte-Carlo
