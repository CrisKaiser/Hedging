
import Global
from OptionPrice import OptionPrice;
import Marketplace

def main():
    

    q = Marketplace.getMarketOptionPrice("2015-10-10", "2015-10-10", "2015-10-20", 200, Global.OType.CALL)
    print(q)

if __name__ == "__main__":
    main()