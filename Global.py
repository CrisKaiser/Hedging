from enum import Enum

INIT_INVEST = 100000
EXP_RETURN = 0.1 #=expected asset drift
HEDGING_MODE = 0 #0 -> Black-Scholes, 1-> Monte-Carlo
HEDING_ASSET = 0 #0-> Hedging with puts; 1-> Hedging with calls

class OType(Enum):
    PUT = 0
    CALL = 1