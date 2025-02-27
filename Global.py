from enum import Enum

EXP_RETURN = 0.02 #=expected asset drift
HEDGING_MODE = 0 #0 -> Black-Scholes, 1-> Monte-Carlo
MATURTIY = 90
VOLATILITY_PREMIUM = 0.1
START_DATE = "2016-01-01"
END_DATE = "2024-12-10"
VOLATILTY_MODE = 1 #0 -> IV, 1 -> HV
INITIAL_INVEST = 1000
MARKET_DATA_LENGTH = 5
TUPEL_DATA_LENGTH = 3
DYNAMIC_INVEST = False #false: rebuild Portfolio with 1000€ invest, true: rebuild Portfolio with initial units

class OType(Enum):
    PUT = 0
    CALL = 1
