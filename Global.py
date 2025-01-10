from enum import Enum

EXP_RETURN = 0.02 #=expected asset drift
HEDGING_MODE = 0 #0 -> Black-Scholes, 1-> Monte-Carlo
MATURTIY = 90
VOLATILITY_PREMIUM = 0.1
START_DATE = "2023-12-01"
END_DATE = "2024-12-10"
VOLATILTY_MODE = 0 #0 -> IV, 1 -> HV
INITIAL_INVEST = 1000
MARKET_DATA_LENGTH = 30
DYNAMIC_INVEST = True #false: rebuild Portfolio with 1000€ invest, true: rebuild Portfolio with initial units

MARKET_CACHE_LENGTH1 = 3
MARKET_CACHE_LENGTH2 = 10
MARKET_CACHE_LENGTH3 = 11

class OType(Enum):
    PUT = 0
    CALL = 1
