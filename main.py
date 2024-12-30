
from Equity import Equity
from Dynamics import Dynamics
from views.EquityView import EquityView
from views.EquityGreekView import EquityGreekView
from views.PortfolioValueView import PortfolioValueView

from Option import Option
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import Global

def main():
    equity = Equity() #model
    dynamics = Dynamics(equity) #controler
    #---views----
    equityView = EquityView(equity)
    equityGreekView = EquityGreekView(equity)
    portfolioValueView = PortfolioValueView(equity.getPortfolio())
    #------------

    dynamics.run()
    equityView.drawStockAndEquity()

    s = Marketplace.getImpliedVolatility("2023-10-11")
    print(s)

if __name__ == "__main__":
    main()