from enum import Enum

INIT_INVEST = 100000
EXP_RETURN = 0.1 #=expected asset drift

class OType(Enum):
    PUT = 0
    CALL = 1