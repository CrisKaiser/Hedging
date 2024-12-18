
import Global
from OptionPrice import OptionPrice;

def main():
    p = OptionPrice()
    q = p.bigLambda("2020-10-10", "2020-11-10", 100, Global.OTpye.CALL)
    print(q)

if __name__ == "__main__":
    main()