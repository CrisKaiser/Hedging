
from Equity import Equity
from Dynamics import Dynamics
from views.EquityView import EquityView
from views.EquityNormalizedView import EquityNormalizedView
from views.PhiView import PhiView

from Option import Option
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta
import Global

def main():
    equity = Equity() #model
    dynamics = Dynamics(equity) #controler
    #---views----
    equityView = EquityView(equity)
    equityNormalizedView = EquityNormalizedView(equity)
    phiView = PhiView(dynamics)
    #------------

    dynamics.run()
    equityNormalizedView.drawStockAndEquity()

if __name__ == "__main__":
    main()