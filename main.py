
from Equity import Equity
from Dynamics import Dynamics
from views.ClearingAccountView import ClearingAccountView
from views.EquityView import EquityView
from views.PortfolioDeltaView import PortfolioDeltaView
from views.PortfolioDistrView import PortfolioDistrView
from views.PortfolioValueView import PortfolioValueView

from Option import Option
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
import Global

def main():
    equity = Equity() #model
    dynamics = Dynamics(equity) #controler
    #---views----
    clearingAccountView = ClearingAccountView(equity.getClearingAccount())
    equityView = EquityView(equity)
    portfolioDeltaView = PortfolioDeltaView(equity.getPortfolio())
    portfolioDistrView = PortfolioDistrView(equity.getPortfolio())
    portfolioValueView = PortfolioValueView(equity.getPortfolio())
    #------------

    dynamics.run()
    #equityView.draw()
    equityView.drawStockAndEquity()
    # o = Option(Global.START_DATE, DateCalc.getDateNDaysAfter(Global.START_DATE, 2), Marketplace.getStockPriceOnDate(Global.START_DATE), Global.OType.CALL)
    # print(o.getMarketValue(DateCalc.getDateNDaysAfter(Global.START_DATE, 1)))

    # s = Global.States.STRONG_CALL
    # q = Global.States(s.value + 1)
    # print(q)

if __name__ == "__main__":
    main()