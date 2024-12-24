import csv
import Global
from datetime import datetime
import random
import numpy as np
import math

class MonteCarlo:
    #const
    file_path = "data/bitcoin_2010-07-17_2024-12-15.csv"

    #default
    _N = 10000
    _sigma = 0.17314693165057277
    _mu = Global.EXP_RETURN

    def calcOptionPrice(self, creation_date, current_date, expire_date, K, optionType, s0):
        return np.exp( self.day_difference(expire_date, current_date) ) * self.monteCarlo(self._N, creation_date, expire_date, K, optionType, s0)

    def calcHedgingPricePairs(self, creation_date, current_date, expire_date, K, optionType, s0, h):
        c = np.exp( self.day_difference(expire_date, current_date) )
        array = self.monteCarloHedging(self._N, creation_date, expire_date, K, optionType, s0, h)
        return  [array[0] *c, array[1] * c]

    def monteCarlo(self, N, creation_date, expire_date, K, optionType, s0):
        _sum = 0
        for i in range(self._N):
            z = self.getZ()
            _z0 = self.bigLambda(creation_date, expire_date, K, optionType, s0, z)
            _z1 = self.bigLambda(creation_date, expire_date, K, optionType, s0, -z)
            _sum += (_z0 + _z1) / 2.0
        return (1. / self._N) * _sum

    def monteCarloHedging(self, N, creation_date, expire_date, K, optionType, s0, h):
        _sumVh = 0.0
        _sumV = 0.0
        for i in range(self._N):
            z = self.getZ()
            _z0 = self.bigLambda(creation_date, expire_date, K, optionType, s0, z)
            _z1 = self.bigLambda(creation_date, expire_date, K, optionType, s0, -z)
            _z0H = self.bigLambda(creation_date, expire_date, K, optionType, s0 + h, z)
            _z1H = self.bigLambda(creation_date, expire_date, K, optionType, s0 + h, -z)
            _sumVh += (_z0H + _z1H) / 2.0
            _sumV += (_z0 + _z1) / 2.0
        return [(1. / self._N) * _sumVh ,(1. / self._N) * _sumV]

    def bigLambda(self, creation_date, expire_date, K, optionType, s0, z):
        T = self.day_difference(creation_date, expire_date)
        futureStockPrice = s0 * np.exp( (self._mu - 0.5*math.pow(self._sigma,2))*T + (self._sigma * math.sqrt(T)* z) )

        if optionType == Global.OType.CALL:
            return max(futureStockPrice - K,0)
        elif optionType == Global.OType.PUT:
            return max(K - futureStockPrice, 0)

    def day_difference(self, date1: str, date2: str) -> int:
        format_str = "%Y-%m-%d"
        date1_obj = datetime.strptime(date1, format_str)
        date2_obj = datetime.strptime(date2, format_str)
        
        diff = float ((date2_obj - date1_obj).days) / 365.2425 #!Jahresrendite
        return diff
    	
    def getZ(self):
        return random.gauss(0, 1)
    