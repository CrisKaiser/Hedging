
from scipy.optimize import brentq

class VolatilitySurface:

    def calculateImpliedVolatility(estimated_price_func,estimateprice):

        def price_diff(sigma):
            return estimated_price_func(sigma) - estimateprice

        try:
            implied_vol = brentq(price_diff, 0.001, 5.0, xtol=1e-6)
            return implied_vol
        except ValueError as e:
            print(f"Fehler bei der Berechnung der impliziten Volatilität: {e}")
            return None

    
    def getVolatility(estimated_price_func,estimateprice):
        return VolatilitySurface.calculateImpliedVolatility(estimated_price_func,estimateprice)
