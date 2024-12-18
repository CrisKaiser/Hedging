
import Global
from OptionPrice import OptionPrice;
import Marketplace

def main():
    

    q = Marketplace.getMarketOptionPrice("2015-10-10", "2015-10-10", "2015-10-20", 250, Global.OType.PUT)
    print(q)

if __name__ == "__main__":
    main()