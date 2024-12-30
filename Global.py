from enum import Enum

EXP_RETURN = 0.02 #=expected asset drift
HEDGING_MODE = 0 #0 -> Black-Scholes, 1-> Monte-Carlo
MATURTIY = 10
VOLATILITY_PREMIUM = 0.2
START_DATE = "2023-05-06"
END_DATE = "2024-12-10"
VOLATILTY_MODE = 0 #0 -> IV, 1 -> HV

class OType(Enum):
    PUT = 0
    CALL = 1

class States(Enum):
    STRONG_CALL = 3
    WEAK_CALL = 2
    WEAK_PUT = 1
    STRONG_PUT = 0