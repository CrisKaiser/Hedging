
import Global
from Option import Option

def main():
    
    o = Option("2015-10-10", "2015-10-11", "2015-10-30", 229, Global.OType.PUT)
    p = o.getMarketValue()
    theta = o.getTheta()
    gamma = o.getGamma()
    vega = o.getVega()
    rho = o.getRho()

    print("Option Price: " + str(p))
    print("Theta: " + str(theta))
    print("Gamma: " + str(gamma))
    print("Vega: " + str(vega))
    print("Rho: " + str(rho))



if __name__ == "__main__":
    main()