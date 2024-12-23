import Global
from datetime import datetime
import numpy as np
import math
import scipy.stats as stats

class BlackScholes:
    file_path = "data/bitcoin_2010-07-17_2024-12-15.csv"

    _sigma = 0.1 #default value
    _r = 0.02 #default value

    def __init__(self, r, sigma):
        self._r = r
        self._sigma = sigma

    def calcOptionPrice(self, creation_date, current_date, expire_date, K, optionType, st):
        if st <= 0:
            raise ValueError("Stockprice negative!")
        if K <= 0:
            raise ValueError("Strikeprice negative!")
        if self.day_difference(current_date, expire_date) <= 0:
            raise ValueError("T negative!")
        
        bigPhiA = self.getBigPhiA(creation_date, current_date, expire_date, K, optionType, st)
        bigPhiB = self.getBigPhiB(creation_date, current_date, expire_date, K, optionType, st)

        if optionType == Global.OType.CALL:
            return st * bigPhiA - K * np.exp(-self._r * self.day_difference(current_date, expire_date)) * bigPhiB
        elif optionType == Global.OType.PUT:
            return K * np.exp(-self._r * self.day_difference(current_date, expire_date)) * (1 - bigPhiB) - st * (1 - bigPhiA)


    def day_difference(self, date1: str, date2: str) -> float:
        format_str = "%Y-%m-%d"
        date1_obj = datetime.strptime(date1, format_str)
        date2_obj = datetime.strptime(date2, format_str)
        return (date2_obj - date1_obj).days / 365.2425  # Jahr basiert auf einem Durchschnitt

    
    def getA(self, creation_date, current_date, expire_date, K, st):
        T = self.day_difference(creation_date, expire_date)
        if T <= 0:
            raise ValueError("T negative!")
        if self._sigma <= 0:
            raise ValueError("Volatility negative!")
    
        _c0 = math.log(st / K)
        _c1 = (self._r + 0.5 * math.pow(self._sigma, 2)) * T
        _c2 = self._sigma * math.sqrt(T)
        return (_c0 + _c1) / _c2


    def getB(self, creation_date, current_date, expire_date, K, st):
        return self.getA(creation_date, current_date, expire_date, K, st) - self._sigma * math.sqrt(self.day_difference(current_date, expire_date))

    def getTheta(self, creation_date, current_date, expire_date, K, optionType, s0, st):
        smallPhiA = self.getSmallPhiA(creation_date, current_date, expire_date, K, optionType, st)
        bigPhiB = self.getBigPhiB(creation_date, current_date, expire_date, K, optionType, st)
        T = self.day_difference(creation_date, expire_date)
            
        if optionType == Global.OType.CALL:
            _c0 = ( s0 * smallPhiA * self._sigma ) / ( 2.0 * math.sqrt(T) )
            _c1 = self._r * K * np.exp(-self._r * T) * bigPhiB
            return _c0 - _c1

        elif optionType == Global.OType.PUT:
            _c0 = ( s0 * smallPhiA * self._sigma ) / ( 2.0 * math.sqrt(T) )
            _c1 = self._r * K * np.exp(-self._r * T) * (1.0 - bigPhiB)
            return _c0 + _c1

    def getGamma(self, creation_date, current_date, expire_date, K, optionType, s0, st):
        smallPhiA = self.getSmallPhiA(creation_date, current_date, expire_date, K, optionType, st)
        T = self.day_difference(creation_date, expire_date)
        return (smallPhiA) / (s0 * self._sigma * math.sqrt(T))

    def getVega(self, creation_date, current_date, expire_date, K, optionType, s0, st):
        smallPhiA = self.getSmallPhiA(creation_date, current_date, expire_date, K, optionType, st)
        T = self.day_difference(creation_date, expire_date)
        return s0 * math.sqrt(T) * smallPhiA

    def getRho(self, creation_date, current_date, expire_date, K, optionType, st):
        bigPhiB = self.getBigPhiB(creation_date, current_date, expire_date, K, optionType, st)
        T = self.day_difference(creation_date, expire_date)
        if optionType == Global.OType.CALL:
            return K * T * np.exp(-self._r * T) * bigPhiB
        elif optionType == Global.OType.PUT:
            return -K * T * np.exp(-self._r * T) * (1.0 - bigPhiB)

    def getBigPhiA(self, creation_date, current_date, expire_date, K, optionType, st):
        return stats.norm.cdf(self.getA(creation_date, current_date, expire_date, K, st))

    def getBigPhiB(self, creation_date, current_date, expire_date, K, optionType, st):
        return stats.norm.cdf(self.getB(creation_date, current_date, expire_date, K, st))

    def getSmallPhiA(self, creation_date, current_date, expire_date, K, optionType, st):
        return stats.norm.pdf(self.getA(creation_date, current_date, expire_date, K, st))

    
    