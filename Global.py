from enum import Enum

EXP_RETURN = 0.02 #=expected asset drift
HEDGING_MODE = 0 #0 -> Black-Scholes, 1-> Monte-Carlo
MATURTIY = 90
VOLATILITY_PREMIUM = 0.2
START_DATE = "2023-03-25"
END_DATE = "2024-12-10"
VOLATILTY_MODE = 0 #0 -> IV, 1 -> HV
INITIAL_INVEST = 1000
MARKET_DATA_LENGTH = 30
MARKET_CACHE1_LENGTH = 5
MARKET_CACHE2_LENGTH = 10
MARKET_CACHE3_LENGTH = 20

class OType(Enum):
    PUT = 0
    CALL = 1

class StatesI(Enum):
    STRONG_CALL = 3
    WEAK_CALL = 2
    WEAK_PUT = 1
    STRONG_PUT = 0

class StatesII(Enum):
    CALL = 1
    PUT = 0

class StatesIII(Enum):
    CALL = 2
    WEAK_PUT = 1
    STRONG_PUT = 0

class StatesIV(Enum):
    STRONG_CALL = 2
    WEAK_CALL = 0, 1
    PUT = -1

class StatesV(Enum):
    INVEST_CALL = 2
    HEDGE_CALL = 1
    HEDGE_PUT = 0