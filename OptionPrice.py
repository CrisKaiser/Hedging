import csv
import Global
from datetime import datetime
import random
import numpy as np
import math

class OptionPrice:
    _N = 100
    file_path = "data/bitcoin_2010-07-17_2024-12-15.csv"

    #literals:
    _sigma = 0.3
    _mu = 0.1

    def __init__(self):
        pass

    def calcOptionPrice(file_path):
        pass


    def bigLambda(self, current_date, date, K, optionType):
        pricesT = self.getHighLowForDate(self.file_path, date);
        s0 = 0.5 * (float(pricesT[0]) + float(pricesT[1]))
        T = self.day_difference(current_date, date)
        futureStockPrice = s0 * np.exp( (self._mu - 0.5*math.pow(self._sigma, 2) ) * T + self._sigma*math.sqrt(T) * self.getZ())

        if optionType == Global.OTpye.CALL:
            return max(futureStockPrice - K,0)
        elif optionType == Global.OTpye.PUT:
            return max(K - futureStockPrice, 0)


    def getHighLowForDate(self, file_path, target_date):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    date = row.get('\ufeffStart')
                    if date == target_date:
                        high_price = row.get('High')
                        low_price = row.get('Low')
                        print(f"Am {target_date}: High = {high_price}, Low = {low_price}")
                        return high_price, low_price

                print(f"Kein Eintrag für das Datum {target_date} gefunden.")
                return None, None

        except FileNotFoundError:
            print(f"Datei nicht gefunden: {file_path}")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            return None, None

    def day_difference(self, date1: str, date2: str) -> int:
        format_str = "%Y-%m-%d"
        date1_obj = datetime.strptime(date1, format_str)
        date2_obj = datetime.strptime(date2, format_str)
        
        diff = (date2_obj - date1_obj).days
        return diff
    	
    def getZ(self):
        return random.gauss(0, 1)
    