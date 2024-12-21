import csv
import Global
from datetime import datetime
import random
import numpy as np
import math
import scipy.stats as stats

class BlackScholes:
    file_path = "data/bitcoin_2010-07-17_2024-12-15.csv"

    _sigma = 0.1 #default value
    _r = 0.02 #default value

    _sharePriceCache = {};

    def __init__(self, r, sigma):
        self._r = r
        self._sigma = sigma
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames

                for row in reader:
                    date = row.get('\ufeffStart')
                    if date:
                        high_price = float(row.get('High', 0))
                        low_price = float(row.get('Low', 0))
                        avg_price = (high_price + low_price) / 2
                        self._sharePriceCache[date] = avg_price

        except FileNotFoundError:
            print(f"Could not find: {self.file_path}")
        except Exception as e:
            print(f"Could not load data: {e}")

    def calcOptionPrice(self, creation_date, current_date, expire_date, K, optionType):
        bigPhiA = stats.norm.cdf(self.getA(creation_date, current_date, expire_date, K), self._r, self._sigma)
        bigPhiB = stats.norm.cdf(self.getB(creation_date, current_date, expire_date, K), self._r, self._sigma)

        if optionType == Global.OType.CALL:
            sT = self.getValueOnDate(current_date)
            return sT * bigPhiA - K * np.exp( -self._r * self.day_difference(current_date, expire_date) )*bigPhiB

        elif optionType == Global.OType.PUT:
            sT = self.getValueOnDate(current_date)
            return sT*(bigPhiB-1.0) - K * np.exp( -self._r * self.day_difference(current_date, expire_date) )*(bigPhiB-1.0)

    def getValueOnDate(self, target_date):
        return self._sharePriceCache[target_date]

    def day_difference(self, date1: str, date2: str) -> int:
        format_str = "%Y-%m-%d"
        date1_obj = datetime.strptime(date1, format_str)
        date2_obj = datetime.strptime(date2, format_str)
        
        diff = float ((date2_obj - date1_obj).days) / 365.2425 #!Jahresrendite
        return diff
    
    def getA(self, creation_date, current_date, expire_date, K):
        T = self.day_difference(creation_date, expire_date)
        sT = self.getValueOnDate(current_date)
        _c0 = math.log(sT /  K)
        _c1 = (self._r + 0.5*math.pow(self._sigma, 2)) * self.day_difference(current_date, expire_date)
        _c2 = self._sigma * math.sqrt(self.day_difference(current_date, expire_date))
        return (_c0 + _c1)/_c2

    def getB(self, creation_date, current_date, expire_date, K):
        return self.getA(creation_date, current_date, expire_date, K) - self._sigma * math.sqrt(self.day_difference(current_date, expire_date))

    def getTheta(self, creation_date, current_date, expire_date, K, optionType):
        smallPhiA = stats.norm.pdf(self.getA(creation_date, current_date, expire_date, K), self._r, self._sigma)
        bigPhiB = stats.norm.cdf(self.getB(creation_date, current_date, expire_date, K), self._r, self._sigma)
        T = self.day_difference(creation_date, expire_date)
        s0 = self.getValueOnDate(creation_date)
            
        if optionType == Global.OType.CALL:
            _c0 = ( s0 * smallPhiA * self._sigma ) / ( 2.0 * math.sqrt(T) )
            _c1 = self._r * K * np.exp(-self._r * T) * bigPhiB
            return _c0 - _c1

        elif optionType == Global.OType.PUT:
            _c0 = ( s0 * smallPhiA * self._sigma ) / ( 2.0 * math.sqrt(T) )
            _c1 = self._r * K * np.exp(-self._r * T) * (1.0 - bigPhiB)
            return _c0 + _c1

    def getGamma(self, creation_date, current_date, expire_date, K, optionType):
        smallPhiA = stats.norm.pdf(self.getA(creation_date, current_date, expire_date, K), self._r, self._sigma)
        T = self.day_difference(creation_date, expire_date)
        s0 = self.getValueOnDate(creation_date)
        return (smallPhiA) / (s0 * self._sigma * math.sqrt(T))

    def getVega(self, creation_date, current_date, expire_date, K, optionType):
        smallPhiA = stats.norm.pdf(self.getA(creation_date, current_date, expire_date, K), self._r, self._sigma)
        T = self.day_difference(creation_date, expire_date)
        s0 = self.getValueOnDate(creation_date)
        return s0 * math.sqrt(T) * smallPhiA

    def getRho(self, creation_date, current_date, expire_date, K, optionType):
        bigPhiB = stats.norm.cdf(self.getB(creation_date, current_date, expire_date, K), self._r, self._sigma)
        T = self.day_difference(creation_date, expire_date)
        if optionType == Global.OType.CALL:
            return K * T * np.exp(-self._r * T) * bigPhiB
        elif optionType == Global.OType.PUT:
            return -K * T * np.exp(-self._r * T) * (1.0 - bigPhiB)