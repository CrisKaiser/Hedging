
from Equity import Equity
from DynamicsI import DynamicsI
from DynamicsII import DynamicsII
from DynamicsIII import DynamicsIII
from DynamicsIV import DynamicsIV
from DynamicsV import DynamicsV
from DynamicsVI import DynamicsVI
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
    dynamics = DynamicsVI(equity) #controler
    #---views----
    equityView = EquityView(equity)
    equityNormalizedView = EquityNormalizedView(equity)
    portfolioValueView = PortfolioValueView(equity.getPortfolio())
    #------------

    dynamics.run()
    equityNormalizedView.drawStockAndEquity()

if __name__ == "__main__":
    main()