
import Global
from framework.Marketplace import Marketplace
from Option import Option

class HedgingDelta:

    @staticmethod
    def calcNewDelta(option: Option, current_date):
        if Global.HEDGING_MODE == 0:
            if option._optionType == Global.OType.CALL:
                return option.getBigPhiA(current_date)
            elif option._optionType == Global.OType.PUT:
                return option.getBigPhiA(current_date) - 1.0

        elif Global.HEDGING_MODE == 1:
            h = 0.4
            array = option.getMonteCarloHedgingPricePairs(h, current_date)
            return (array[0] - array[1]) / h
