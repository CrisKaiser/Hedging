
from Equity import Equity
from Dynamics import Dynamics
from views.ClearingAccountView import ClearingAccountView
from views.EquityView import EquityView
from views.PortfolioDeltaView import PortfolioDeltaView
from views.PortfolioDistrView import PortfolioDistrView
from views.PortfolioValueView import PortfolioValueView

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

    

if __name__ == "__main__":
    main()