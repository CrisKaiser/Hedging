
import Global
import Marketplace
from Option import Option

class HedgingDelta:

    def __init__(self):
        pass

    def calcNewDelta(self, option: Option, ):
        if Global.HEDGING_MODE == 0:
            #Black-Scholes
            pass

        elif Global.HEDGING_MODE == 1:
            #Monte-Carlo
            pass
