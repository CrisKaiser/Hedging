
import Global
from framework.DateCalc import DateCalc
from framework.Marketplace import Marketplace
from framework.LinearRegression import LinearRegression
import numpy as np
from numpy.linalg import norm

class DynamicsII:
    _equity = None
    _current_date = Global.START_DATE

    _marketCache1 = np.zeros(1).tolist()
    _marketCache2 = np.zeros(2).tolist()
    _marketCache3 = np.zeros(3).tolist()
    _marketCache4 = np.zeros(4).tolist()
    _marketCache5 = np.zeros(5).tolist()
    _marketCache6 = np.zeros(6).tolist()
    _marketCache7 = np.zeros(7).tolist()
    _marketCache8 = np.zeros(8).tolist()
    _marketCache9 = np.zeros(9).tolist()
    _marketCache10 = np.zeros(10).tolist()
    _marketCache11 = np.zeros(11).tolist()
    _marketCache12 = np.zeros(12).tolist()
    _marketCache13 = np.zeros(13).tolist()
    _marketCache14 = np.zeros(14).tolist()
    _marketCache15 = np.zeros(15).tolist()
    _marketCache16 = np.zeros(16).tolist()
    _marketCache17 = np.zeros(17).tolist()
    _marketCache18 = np.zeros(18).tolist()
    _marketCache19 = np.zeros(19).tolist()
    _marketCache20 = np.zeros(20).tolist()
    _marketCache21 = np.zeros(21).tolist()
    _marketCache22 = np.zeros(22).tolist()
    _marketCache23 = np.zeros(23).tolist()
    _marketCache24 = np.zeros(24).tolist()
    _marketCache25 = np.zeros(25).tolist()
    _marketCache26 = np.zeros(26).tolist()
    _marketCache27 = np.zeros(27).tolist()
    _marketCache28 = np.zeros(28).tolist()
    _marketCache29 = np.zeros(29).tolist()
    _marketCache30 = np.zeros(30).tolist()
    _marketCache31 = np.zeros(31).tolist()
    _marketCache32 = np.zeros(32).tolist()
    _marketCache33 = np.zeros(33).tolist()
    _marketCache34 = np.zeros(34).tolist()
    _marketCache35 = np.zeros(35).tolist()
    _marketCache36 = np.zeros(36).tolist()
    _marketCache37 = np.zeros(37).tolist()
    _marketCache38 = np.zeros(38).tolist()
    _marketCache39 = np.zeros(39).tolist()
    _marketCache40 = np.zeros(40).tolist()
    _marketCache41 = np.zeros(41).tolist()
    _marketCache42 = np.zeros(42).tolist()
    _marketCache43 = np.zeros(43).tolist()
    _marketCache44 = np.zeros(44).tolist()
    _marketCache45 = np.zeros(45).tolist()
    _marketCache46 = np.zeros(46).tolist()
    _marketCache47 = np.zeros(47).tolist()
    _marketCache48 = np.zeros(48).tolist()
    _marketCache49 = np.zeros(49).tolist()
    _marketCache50 = np.zeros(50).tolist()
    _marketCache51 = np.zeros(51).tolist()
    _marketCache52 = np.zeros(52).tolist()
    _marketCache53 = np.zeros(53).tolist()
    _marketCache54 = np.zeros(54).tolist()
    _marketCache55 = np.zeros(55).tolist()
    _marketCache56 = np.zeros(56).tolist()
    _marketCache57 = np.zeros(57).tolist()
    _marketCache58 = np.zeros(58).tolist()
    _marketCache59 = np.zeros(59).tolist()
    _marketCache60 = np.zeros(60).tolist()
    _marketCache61 = np.zeros(61).tolist()
    _marketCache62 = np.zeros(62).tolist()
    _marketCache63 = np.zeros(63).tolist()
    _marketCache64 = np.zeros(64).tolist()
    _marketCache65 = np.zeros(65).tolist()
    _marketCache66 = np.zeros(66).tolist()
    _marketCache67 = np.zeros(67).tolist()
    _marketCache68 = np.zeros(68).tolist()
    _marketCache69 = np.zeros(69).tolist()
    _marketCache70 = np.zeros(70).tolist()
    _marketCache71 = np.zeros(71).tolist()
    _marketCache72 = np.zeros(72).tolist()
    _marketCache73 = np.zeros(73).tolist()
    _marketCache74 = np.zeros(74).tolist()
    _marketCache75 = np.zeros(75).tolist()
    _marketCache76 = np.zeros(76).tolist()
    _marketCache77 = np.zeros(77).tolist()
    _marketCache78 = np.zeros(78).tolist()
    _marketCache79 = np.zeros(79).tolist()
    _marketCache80 = np.zeros(80).tolist()
    _marketCache81 = np.zeros(81).tolist()
    _marketCache82 = np.zeros(82).tolist()
    _marketCache83 = np.zeros(83).tolist()
    _marketCache84 = np.zeros(84).tolist()
    _marketCache85 = np.zeros(85).tolist()
    _marketCache86 = np.zeros(86).tolist()
    _marketCache87 = np.zeros(87).tolist()
    _marketCache88 = np.zeros(88).tolist()
    _marketCache89 = np.zeros(89).tolist()
    _marketCache90 = np.zeros(90).tolist()
    _marketCache91 = np.zeros(91).tolist()
    _marketCache92 = np.zeros(92).tolist()
    _marketCache93 = np.zeros(93).tolist()
    _marketCache94 = np.zeros(94).tolist()
    _marketCache95 = np.zeros(95).tolist()
    _marketCache96 = np.zeros(96).tolist()
    _marketCache97 = np.zeros(97).tolist()
    _marketCache98 = np.zeros(98).tolist()
    _marketCache99 = np.zeros(99).tolist()
    _marketCache100 = np.zeros(100).tolist()

    _marketDataSet = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
    _marketDictionary = {}
    _views = []
    _bigPhi = None
    
    def __init__(self, equity):
        if equity == None:
            raise ValueError("Equity is null")
        self._equity = equity
        self.preload()
        print("Market Data loaded")

    def run(self):
        while(not DateCalc.areDatesEqual(self._current_date, Global.END_DATE)):
            self.equityUpdate()
            self._current_date = DateCalc.getDateNDaysAfter(self._current_date, 1)
        print(self._equity.getEquity(self._current_date))
        
    def equityUpdate(self):
        res = self.bigPi(self._current_date)
        if res > 0.55:
            self._equity.hedge(self._current_date, Global.OType.CALL)
        else:
            self._equity.hedge(self._current_date, Global.OType.PUT)

    def fillMarketDataSet(self, current_date):
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketDataSet[i] = self.isStockIncreasing(new_date)

    def fillCaches(self, current_date):
        for i in range(1):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache1[i] = self.isStockIncreasing(new_date)
        for i in range(2):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache2[i] = self.isStockIncreasing(new_date)
        for i in range(3):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache3[i] = self.isStockIncreasing(new_date)
        for i in range(4):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache4[i] = self.isStockIncreasing(new_date)
        for i in range(5):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache5[i] = self.isStockIncreasing(new_date)
        for i in range(6):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache6[i] = self.isStockIncreasing(new_date)
        for i in range(7):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache7[i] = self.isStockIncreasing(new_date)
        for i in range(8):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache8[i] = self.isStockIncreasing(new_date)
        for i in range(9):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache9[i] = self.isStockIncreasing(new_date)
        for i in range(10):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache10[i] = self.isStockIncreasing(new_date)

        for i in range(11):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache11[i] = self.isStockIncreasing(new_date)
        for i in range(12):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache12[i] = self.isStockIncreasing(new_date)
        for i in range(13):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache13[i] = self.isStockIncreasing(new_date)
        for i in range(14):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache14[i] = self.isStockIncreasing(new_date)
        for i in range(15):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache15[i] = self.isStockIncreasing(new_date)
        for i in range(16):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache16[i] = self.isStockIncreasing(new_date)
        for i in range(17):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache17[i] = self.isStockIncreasing(new_date)
        for i in range(18):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache18[i] = self.isStockIncreasing(new_date)
        for i in range(19):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache19[i] = self.isStockIncreasing(new_date)
        for i in range(20):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache20[i] = self.isStockIncreasing(new_date)

        for i in range(21):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache21[i] = self.isStockIncreasing(new_date)
        for i in range(22):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache22[i] = self.isStockIncreasing(new_date)
        for i in range(23):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache23[i] = self.isStockIncreasing(new_date)
        for i in range(24):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache24[i] = self.isStockIncreasing(new_date)
        for i in range(25):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache25[i] = self.isStockIncreasing(new_date)
        for i in range(26):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache26[i] = self.isStockIncreasing(new_date)
        for i in range(27):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache27[i] = self.isStockIncreasing(new_date)
        for i in range(28):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache28[i] = self.isStockIncreasing(new_date)
        for i in range(29):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache29[i] = self.isStockIncreasing(new_date)
        for i in range(30):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache30[i] = self.isStockIncreasing(new_date)

        for i in range(31):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache31[i] = self.isStockIncreasing(new_date)
        for i in range(32):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache32[i] = self.isStockIncreasing(new_date)
        for i in range(33):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache33[i] = self.isStockIncreasing(new_date)
        for i in range(34):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache34[i] = self.isStockIncreasing(new_date)
        for i in range(35):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache35[i] = self.isStockIncreasing(new_date)
        for i in range(36):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache36[i] = self.isStockIncreasing(new_date)
        for i in range(37):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache37[i] = self.isStockIncreasing(new_date)
        for i in range(38):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache38[i] = self.isStockIncreasing(new_date)
        for i in range(39):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache39[i] = self.isStockIncreasing(new_date)
        for i in range(40):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache40[i] = self.isStockIncreasing(new_date)

        for i in range(41):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache41[i] = self.isStockIncreasing(new_date)
        for i in range(42):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache42[i] = self.isStockIncreasing(new_date)
        for i in range(43):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache43[i] = self.isStockIncreasing(new_date)
        for i in range(44):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache44[i] = self.isStockIncreasing(new_date)
        for i in range(45):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache45[i] = self.isStockIncreasing(new_date)
        for i in range(46):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache46[i] = self.isStockIncreasing(new_date)
        for i in range(47):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache47[i] = self.isStockIncreasing(new_date)
        for i in range(48):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache48[i] = self.isStockIncreasing(new_date)
        for i in range(49):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache49[i] = self.isStockIncreasing(new_date)
        for i in range(50):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache50[i] = self.isStockIncreasing(new_date)

        for i in range(51):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache51[i] = self.isStockIncreasing(new_date)
        for i in range(52):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache52[i] = self.isStockIncreasing(new_date)
        for i in range(53):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache53[i] = self.isStockIncreasing(new_date)
        for i in range(54):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache54[i] = self.isStockIncreasing(new_date)
        for i in range(55):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache55[i] = self.isStockIncreasing(new_date)
        for i in range(56):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache56[i] = self.isStockIncreasing(new_date)
        for i in range(57):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache57[i] = self.isStockIncreasing(new_date)
        for i in range(58):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache58[i] = self.isStockIncreasing(new_date)
        for i in range(59):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache59[i] = self.isStockIncreasing(new_date)
        for i in range(60):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache60[i] = self.isStockIncreasing(new_date)

        for i in range(61):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache61[i] = self.isStockIncreasing(new_date)
        for i in range(62):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache62[i] = self.isStockIncreasing(new_date)
        for i in range(63):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache63[i] = self.isStockIncreasing(new_date)
        for i in range(64):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache64[i] = self.isStockIncreasing(new_date)
        for i in range(65):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache65[i] = self.isStockIncreasing(new_date)
        for i in range(66):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache66[i] = self.isStockIncreasing(new_date)
        for i in range(67):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache67[i] = self.isStockIncreasing(new_date)
        for i in range(68):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache68[i] = self.isStockIncreasing(new_date)
        for i in range(69):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache69[i] = self.isStockIncreasing(new_date)
        for i in range(70):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache70[i] = self.isStockIncreasing(new_date)

        for i in range(71):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache71[i] = self.isStockIncreasing(new_date)
        for i in range(72):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache72[i] = self.isStockIncreasing(new_date)
        for i in range(73):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache73[i] = self.isStockIncreasing(new_date)
        for i in range(74):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache74[i] = self.isStockIncreasing(new_date)
        for i in range(75):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache75[i] = self.isStockIncreasing(new_date)
        for i in range(76):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache76[i] = self.isStockIncreasing(new_date)
        for i in range(77):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache77[i] = self.isStockIncreasing(new_date)
        for i in range(78):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache78[i] = self.isStockIncreasing(new_date)
        for i in range(79):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache79[i] = self.isStockIncreasing(new_date)
        for i in range(80):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache80[i] = self.isStockIncreasing(new_date)

        for i in range(81):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache81[i] = self.isStockIncreasing(new_date)
        for i in range(82):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache82[i] = self.isStockIncreasing(new_date)
        for i in range(83):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache83[i] = self.isStockIncreasing(new_date)
        for i in range(84):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache84[i] = self.isStockIncreasing(new_date)
        for i in range(85):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache85[i] = self.isStockIncreasing(new_date)
        for i in range(86):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache86[i] = self.isStockIncreasing(new_date)
        for i in range(87):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache87[i] = self.isStockIncreasing(new_date)
        for i in range(88):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache88[i] = self.isStockIncreasing(new_date)
        for i in range(89):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache89[i] = self.isStockIncreasing(new_date)
        for i in range(90):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache90[i] = self.isStockIncreasing(new_date)

        for i in range(91):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache91[i] = self.isStockIncreasing(new_date)
        for i in range(92):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache92[i] = self.isStockIncreasing(new_date)
        for i in range(93):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache93[i] = self.isStockIncreasing(new_date)
        for i in range(94):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache94[i] = self.isStockIncreasing(new_date)
        for i in range(95):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache95[i] = self.isStockIncreasing(new_date)
        for i in range(96):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache96[i] = self.isStockIncreasing(new_date)
        for i in range(97):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache97[i] = self.isStockIncreasing(new_date)
        for i in range(98):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache98[i] = self.isStockIncreasing(new_date)
        for i in range(99):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache99[i] = self.isStockIncreasing(new_date)
        for i in range(100):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            self._marketCache100[i] = self.isStockIncreasing(new_date)

    def getSigmas(self, date):
        self.fillCaches(date)
        sigma1 = sum(self._marketCache1) / 1
        sigma2 = sum(self._marketCache2) / 2
        sigma3 = sum(self._marketCache3) / 3
        sigma4 = sum(self._marketCache4) / 4
        sigma5 = sum(self._marketCache5) / 5
        sigma6 = sum(self._marketCache6) / 6
        sigma7 = sum(self._marketCache7) / 7
        sigma8 = sum(self._marketCache8) / 8
        sigma9 = sum(self._marketCache9) / 9
        sigma10 = sum(self._marketCache10) / 10

        sigma11 = sum(self._marketCache11) / 11
        sigma12 = sum(self._marketCache12) / 12
        sigma13 = sum(self._marketCache13) / 13
        sigma14 = sum(self._marketCache14) / 14
        sigma15 = sum(self._marketCache15) / 15
        sigma16 = sum(self._marketCache16) / 16
        sigma17 = sum(self._marketCache17) / 17
        sigma18 = sum(self._marketCache18) / 18
        sigma19 = sum(self._marketCache19) / 19
        sigma20 = sum(self._marketCache20) / 20

        sigma21 = sum(self._marketCache21) / 21
        sigma22 = sum(self._marketCache22) / 22
        sigma23 = sum(self._marketCache23) / 23
        sigma24 = sum(self._marketCache24) / 24
        sigma25 = sum(self._marketCache25) / 25
        sigma26 = sum(self._marketCache26) / 26
        sigma27 = sum(self._marketCache27) / 27
        sigma28 = sum(self._marketCache28) / 28
        sigma29 = sum(self._marketCache29) / 29
        sigma30 = sum(self._marketCache30) / 30

        sigma31 = sum(self._marketCache31) / 31
        sigma32 = sum(self._marketCache32) / 32
        sigma33 = sum(self._marketCache33) / 33
        sigma34 = sum(self._marketCache34) / 34
        sigma35 = sum(self._marketCache35) / 35
        sigma36 = sum(self._marketCache36) / 36
        sigma37 = sum(self._marketCache37) / 37
        sigma38 = sum(self._marketCache38) / 38
        sigma39 = sum(self._marketCache39) / 39
        sigma40 = sum(self._marketCache40) / 40

        sigma41 = sum(self._marketCache41) / 41
        sigma42 = sum(self._marketCache42) / 42
        sigma43 = sum(self._marketCache43) / 43
        sigma44 = sum(self._marketCache44) / 44
        sigma45 = sum(self._marketCache45) / 45
        sigma46 = sum(self._marketCache46) / 46
        sigma47 = sum(self._marketCache47) / 47
        sigma48 = sum(self._marketCache48) / 48
        sigma49 = sum(self._marketCache49) / 49
        sigma50 = sum(self._marketCache50) / 50

        sigma51 = sum(self._marketCache51) / 51
        sigma52 = sum(self._marketCache52) / 52
        sigma53 = sum(self._marketCache53) / 53
        sigma54 = sum(self._marketCache54) / 54
        sigma55 = sum(self._marketCache55) / 55
        sigma56 = sum(self._marketCache56) / 56
        sigma57 = sum(self._marketCache57) / 57
        sigma58 = sum(self._marketCache58) / 58
        sigma59 = sum(self._marketCache59) / 59
        sigma60 = sum(self._marketCache60) / 60

        sigma61 = sum(self._marketCache61) / 61
        sigma62 = sum(self._marketCache62) / 62
        sigma63 = sum(self._marketCache63) / 63
        sigma64 = sum(self._marketCache64) / 64
        sigma65 = sum(self._marketCache65) / 65
        sigma66 = sum(self._marketCache66) / 66
        sigma67 = sum(self._marketCache67) / 67
        sigma68 = sum(self._marketCache68) / 68
        sigma69 = sum(self._marketCache69) / 69
        sigma70 = sum(self._marketCache70) / 70

        sigma71 = sum(self._marketCache71) / 71
        sigma72 = sum(self._marketCache72) / 72
        sigma73 = sum(self._marketCache73) / 73
        sigma74 = sum(self._marketCache74) / 74
        sigma75 = sum(self._marketCache75) / 75
        sigma76 = sum(self._marketCache76) / 76
        sigma77 = sum(self._marketCache77) / 77
        sigma78 = sum(self._marketCache78) / 78
        sigma79 = sum(self._marketCache79) / 79
        sigma80 = sum(self._marketCache80) / 80

        sigma81 = sum(self._marketCache81) / 81
        sigma82 = sum(self._marketCache82) / 82
        sigma83 = sum(self._marketCache83) / 83
        sigma84 = sum(self._marketCache84) / 84
        sigma85 = sum(self._marketCache85) / 85
        sigma86 = sum(self._marketCache86) / 86
        sigma87 = sum(self._marketCache87) / 87
        sigma88 = sum(self._marketCache88) / 88
        sigma89 = sum(self._marketCache89) / 89
        sigma90 = sum(self._marketCache90) / 90

        sigma91 = sum(self._marketCache91) / 91
        sigma92 = sum(self._marketCache92) / 92
        sigma93 = sum(self._marketCache93) / 93
        sigma94 = sum(self._marketCache94) / 94
        sigma95 = sum(self._marketCache95) / 95
        sigma96 = sum(self._marketCache96) / 96
        sigma97 = sum(self._marketCache97) / 97
        sigma98 = sum(self._marketCache98) / 98
        sigma99 = sum(self._marketCache99) / 99
        sigma100 = sum(self._marketCache100) / 100

        res = [
            sigma1, sigma2, sigma3, sigma4, sigma5, sigma6, sigma7, sigma8, sigma9, sigma10,
            sigma11, sigma12, sigma13, sigma14, sigma15, sigma16, sigma17, sigma18, sigma19, sigma20,
            sigma21, sigma22, sigma23, sigma24, sigma25, sigma26, sigma27, sigma28, sigma29, sigma30,
            sigma31, sigma32, sigma33, sigma34, sigma35, sigma36, sigma37, sigma38, sigma39, sigma40,
            sigma41, sigma42, sigma43, sigma44, sigma45, sigma46, sigma47, sigma48, sigma49, sigma50,
            sigma51, sigma52, sigma53, sigma54, sigma55, sigma56, sigma57, sigma58, sigma59, sigma60,
            sigma61, sigma62, sigma63, sigma64, sigma65, sigma66, sigma67, sigma68, sigma69, sigma70,
            sigma71, sigma72, sigma73, sigma74, sigma75, sigma76, sigma77, sigma78, sigma79, sigma80,
            sigma81, sigma82, sigma83, sigma84, sigma85, sigma86, sigma87, sigma88, sigma89, sigma90,
            sigma91, sigma92, sigma93, sigma94, sigma95, sigma96, sigma97, sigma98, sigma99, sigma100
        ]
        return res / norm(res)

    def bigPi(self, current_date):
        self.fillMarketDataSet(self._current_date)
        print(self._marketDataSet)
        matrix = np.zeros(Global.MARKET_DATA_LENGTH).tolist()
        for i in range(Global.MARKET_DATA_LENGTH):
            new_date = DateCalc.getDateNDaysAfter(current_date, -i)
            matrix[i] = self.getSigmas(new_date)
        coVec = LinearRegression.calcSolutionVector(matrix, self._marketDataSet)
        print(coVec)
        currentSigma = self.getSigmas(current_date)
        sum = 0
        for i in range(100):
            sum += coVec[i] * currentSigma[i]
        self._bigPhi = sum
        self.notifyViews(current_date)
        print(current_date)
        return sum

    def isStockIncreasing(self, current_date):
        _yesterday = DateCalc.getDateNDaysAfter(current_date, -1)
        if self._marketDictionary[current_date] > self._marketDictionary[_yesterday]:
            return 1
        else:
            return 0

    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))

    def preload(self):
        _date = DateCalc.getDateNDaysAfter(Global.START_DATE, -(Global.MARKET_DATA_LENGTH + 100) )
        while not DateCalc.areDatesEqual(_date, Global.END_DATE):
            self._marketDictionary[_date] = Marketplace.getStockPriceOnDate(_date)
            _date = DateCalc.getDateNDaysAfter(_date, 1)
    
    def viewRegister(self, view):
        self._views.append(view)

    def notifyViews(self, current_date):
        for view in self._views:
            view.updateView(current_date)
