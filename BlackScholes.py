import csv
import Global
from datetime import datetime
import random
import numpy as np
import math
import scipy.stats as stats

class BlackScholes:
    file_path = "data/bitcoin_2010-07-17_2024-12-15.csv"

    _sigma = 0.1 #reflects course volatility
    _r = 0.02 #ezb yield

    def __init__(self, r, sigma):
        self._r = r
        self.sigma = sigma

    def calcOptionPrice(self, creation_date, current_date, expire_date, K, optionType):
        bigPhiA = stats.norm.cdf(self.getA(creation_date, current_date, expire_date, K), self._r, self._sigma)
        bigPhiB = stats.norm.cdf(self.getB(creation_date, current_date, expire_date, K), self._r, self._sigma)

        if optionType == Global.OType.CALL:
            pricesT = self.getHighLowForDate(self.file_path, current_date)
            sT = sT = 0.5 * (float(pricesT[0]) + float(pricesT[1]))
            return sT * bigPhiA - K * np.exp( -self._r * self.day_difference(current_date, expire_date) )*bigPhiB

        elif optionType == Global.OType.PUT:
            return -1;


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

    def day_difference(self, date1: str, date2: str) -> int:
        format_str = "%Y-%m-%d"
        date1_obj = datetime.strptime(date1, format_str)
        date2_obj = datetime.strptime(date2, format_str)
        
        diff = float ((date2_obj - date1_obj).days) / 365.0 #!Jahresrendite
        return diff
    
    def getA(self, creation_date, current_date, expire_date, K):
        T = self.day_difference(creation_date, expire_date)
        pricesT = self.getHighLowForDate(self.file_path, current_date)
        sT = sT = 0.5 * (float(pricesT[0]) + float(pricesT[1]))
        _c0 = math.log(sT /  K)
        _c1 = (self._r + 0.5*math.pow(self._sigma, 2)) * self.day_difference(current_date, expire_date)
        _c2 = self._sigma * math.sqrt(self.day_difference(current_date, expire_date))
        return (_c0 + _c1)/_c2

    def getB(self, creation_date, current_date, expire_date, K):
        return self.getA(creation_date, current_date, expire_date, K) - self._sigma * math.sqrt(self.day_difference(current_date, expire_date))