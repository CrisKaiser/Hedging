
from Equity import Equity
from DynamicsI import DynamicsI
from DynamicsII import DynamicsII
from DynamicsIII import DynamicsIII
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
    dynamics = DynamicsI(equity) #controler
    #---views----
    equityView = EquityView(equity)
    equityNormalizedView = EquityNormalizedView(equity)
    phiView = PhiView(dynamics)
    #------------

    dynamics.run()
    equityNormalizedView.drawSE()
    phiView.draw()

if __name__ == "__main__":
    main()