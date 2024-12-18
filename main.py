
import Global
from OptionPrice import OptionPrice;
from BlackScholes import BlackScholes; 

def main():
    p = OptionPrice()
    bs = BlackScholes()
   # mc1 = p.calcOptionPrice("2020-10-10", "2020-10-11", "2020-10-15",10000, Global.OType.CALL) 
   # mc2 = p.calcOptionPrice("2020-10-10", "2020-10-12", "2020-10-15",10000, Global.OType.CALL) 
   # mc3 = p.calcOptionPrice("2020-10-10", "2020-10-13", "2020-10-15",10000, Global.OType.CALL) 
   # mc4 = p.calcOptionPrice("2020-10-10", "2020-10-14", "2020-10-15",10000, Global.OType.CALL) 

   # bs1 = bs.calcOptionPrice("2020-10-10", "2020-10-11", "2020-10-15",10000, Global.OType.CALL)
    bs2 = bs.calcOptionPrice("2020-10-10", "2020-10-12", "2020-10-15",10000, Global.OType.CALL)
    #bs3 = bs.calcOptionPrice("2020-10-10", "2020-10-13", "2020-10-15",10000, Global.OType.CALL)
   # bs4 = bs.calcOptionPrice("2020-10-10", "2020-10-14", "2020-10-15",10000, Global.OType.CALL)

  #  print("mc1 is: " + str(mc1))
   # print("mc2 is: " + str(mc2))
    #print("mc3 is: " + str(mc3))
    #print("mc4 is: " + str(mc4))

    #print("bs1 is: " + str(bs1))
    print("bs2 is: " + str(bs2))
   # print("bs3 is: " + str(bs3))
   # print("bs4 is: " + str(bs4))

if __name__ == "__main__":
    main()