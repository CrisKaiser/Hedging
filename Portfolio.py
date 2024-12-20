
import csv
from datetime import datetime

class Portfolio:

    #const
    file_path = "data/bitcoin_2010-07-17_2024-12-15.csv"

    #store var
    _assetQuantity = 0.0
    _optionContainer = []


    def __init__(self):
        pass

    def update(self):
        #{
            #update asset quantity and Options
        #}
        pass

    def getValue(self, current_date):
        pricesT = self.getHighLowForDate(self.file_path, current_date)
        sT = sT = 0.5 * (float(pricesT[0]) + float(pricesT[1]))
        _sum = 0.0
        for i in range(len(self._optionContainer)):
            _sum += self._optionContainer[i].getValue()
        return sT + _sum

    def getPortfolioGamma(self):
        #{
            #update portfolio gamma
        #}
        pass

    def getPortfolioVega(self):
        #{
            #update portfolio vega
        #}
        pass

    def getPortfolioRho(self):
        #{
            #update portfolio rho
        #}
        pass

    def getPortfolioTheta(self):
        #{
            #update portfolio theta
        #}
        pass

    def getHighLowForDate(self, file_path, target_date):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    date = row.get('\ufeffStart')
                    if date == target_date:
                        high_price = row.get('High')
                        low_price = row.get('Low')
                        return high_price, low_price

                print(f"No enty for date: {target_date} .")
                return None, None

        except FileNotFoundError:
            print(f"Could not find: {file_path}")
        except Exception as e:
            print(f"Could not find: {e}")
            return None, None
