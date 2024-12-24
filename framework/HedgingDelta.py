
import Global
from framework.Marketplace import Marketplace
from Option import Option

class HedgingDelta:

    @staticmethod
    def calcNewDelta(option: Option):
        if Global.HEDGING_MODE == 0:
            if option._optionType == Global.OType.CALL:
                return option.getBigPhiA()
            elif option._optionType == Global.OType.PUT:
                return option.getBigPhiA() - 1.0

        elif Global.HEDGING_MODE == 1:
            h = 0.4
            Vh = option.getMonteCarloHedgingValue(h)
            V = option.getMonteCarloValue()
            return (Vh - V) / h
