from enum import Enum

EXP_RETURN = 0.02 #=expected asset drift
HEDGING_MODE = 0 #0 -> Black-Scholes, 1-> Monte-Carlo
MATURTIY = 2
START_DATE = "2015-11-06"
END_DATE = "2016-12-30"

class OType(Enum):
    PUT = 0
    CALL = 1