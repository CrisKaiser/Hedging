from enum import Enum

EXP_RETURN = 0.02 #=expected asset drift
HEDGING_MODE = 0 #0 -> Black-Scholes, 1-> Monte-Carlo
MATURTIY = 2 #smaller than 5
START_DATE = "2017-12-16"
END_DATE = "2018-12-07"

class OType(Enum):
    PUT = 0
    CALL = 1

class States(Enum):
    STRONG_CALL = 3
    WEAK_CALL = 2
    WEAK_PUT = 1
    STRONG_PUT = 0