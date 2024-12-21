
import Global
from MonteCarlo import MonteCarlo
import Marketplace

def main():
    

    p = Marketplace.getMarketOptionPrice("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    theta = Marketplace.getMarketOptionTheta("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    gamma = Marketplace.getMarketOptionGamma("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    vega = Marketplace.getMarketOptionVega("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    rho = Marketplace.getMarketOptionRho("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    greeks = Marketplace.getMarketOptionGreeks("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    print("Option Price: " + str(p))
    print("Theta: " + str(theta))
    print("Gamma: " + str(gamma))
    print("Vega: " + str(vega))
    print("Rho: " + str(rho))

    print(str(greeks))

    s = Marketplace.getMonteCarloPrice("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    print(s)



if __name__ == "__main__":
    main()