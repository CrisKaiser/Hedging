
import Global
from OptionPrice import OptionPrice;

def main():
    p = OptionPrice()
    q = p.calcOptionPrice("2020-10-10", "2020-10-12", "2020-10-20",100, Global.OTpye.CALL)  
    print("q is: " + str(q))

if __name__ == "__main__":
    main()