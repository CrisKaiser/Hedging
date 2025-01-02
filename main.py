
from Equity import Equity
from DynamicsI import DynamicsI
from DynamicsII import DynamicsII
from DynamicsIII import DynamicsIII
from DynamicsIV import DynamicsIV
from DynamicsV import DynamicsV
from views.EquityView import EquityView
from views.EquityNormalizedView import EquityNormalizedView
from views.PortfolioValueView import PortfolioValueView

from Option import Option
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.HedgingDelta import HedgingDelta
import Global

def main():
    equity = Equity() #model
    dynamics = DynamicsV(equity) #controler
    #---views----
    equityView = EquityView(equity)
    equityNormalizedView = EquityNormalizedView(equity)
    portfolioValueView = PortfolioValueView(equity.getPortfolio())
    #------------

    dynamics.run()
    equityNormalizedView.drawSEIV()

if __name__ == "__main__":
    main()