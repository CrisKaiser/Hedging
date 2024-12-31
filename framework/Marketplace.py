import pandas as pd
from framework.BlackScholes import BlackScholes; 
import csv
from framework.MonteCarlo import MonteCarlo
import Global
from framework.DateCalc import DateCalc

file_path = r"data\interest_rates.csv"
file_path_stock = r"data\bitcoin_2010-07-17_2024-12-15.csv"
file_path_volatility = r"data\bitcoin_volatility.csv"
file_path_implied_volatility = r"data\dvol_data.csv"

class Marketplace:

    @staticmethod
    def getMarketOptionPrice(creation_date, current_date, expire_date, K, optionType):
        if DateCalc.isDateBefore(current_date, expire_date):
            _sigma = None
            if Global.VOLATILTY_MODE == 1:
                _sigma = Marketplace.getImpliedVolatility(creation_date)
            else:
                _sigma = Marketplace.getHistoricalVolatility(creation_date)
            _r = Marketplace.get_yield_for_date(current_date)
            bs = BlackScholes(_r, _sigma)
            st = Marketplace.getStockPriceOnDate(current_date)
            return bs.calcOptionPrice(creation_date, current_date, expire_date, K, optionType, st)
        else:
            stockPrice = Marketplace.getStockPriceOnDate(current_date)
            if optionType == Global.OType.CALL:
                return max(stockPrice - K, 0)
            else:
                return max(K - stockPrice, 0)

    @staticmethod
    def getMarketOptionTheta(creation_date, current_date, expire_date, K, optionType):
        _sigma = None
        if Global.VOLATILTY_MODE == 1:
            _sigma = Marketplace.getImpliedVolatility(creation_date)
        else:
            _sigma = Marketplace.getHistoricalVolatility(creation_date)
        _r = Marketplace.get_yield_for_date(current_date)
        bs = BlackScholes(_r, _sigma)
        s0 = Marketplace.getStockPriceOnDate(creation_date)
        st = Marketplace.getStockPriceOnDate(current_date)
        return bs.getTheta(creation_date, current_date, expire_date, K, optionType, s0, st)

    @staticmethod
    def getMarketOptionGamma(creation_date, current_date, expire_date, K, optionType):
        _sigma = None
        if Global.VOLATILTY_MODE == 1:
            _sigma = Marketplace.getImpliedVolatility(creation_date)
        else:
            _sigma = Marketplace.getHistoricalVolatility(creation_date)
        _r = Marketplace.get_yield_for_date(current_date)
        bs = BlackScholes(_r, _sigma)
        s0 = Marketplace.getStockPriceOnDate(creation_date)
        st = Marketplace.getStockPriceOnDate(current_date)
        return bs.getGamma(creation_date, current_date, expire_date, K, optionType, s0, st)

    @staticmethod
    def getMarketOptionVega(creation_date, current_date, expire_date, K, optionType):
        _sigma = None
        if Global.VOLATILTY_MODE == 1:
            _sigma = Marketplace.getImpliedVolatility(creation_date)
        else:
            _sigma = Marketplace.getHistoricalVolatility(creation_date)
        _r = Marketplace.get_yield_for_date(current_date)
        bs = BlackScholes(_r, _sigma)
        s0 = Marketplace.getStockPriceOnDate(creation_date)
        st = Marketplace.getStockPriceOnDate(current_date)
        return bs.getVega(creation_date, current_date, expire_date, K, optionType, s0, st)

    @staticmethod
    def getMarketOptionRho(creation_date, current_date, expire_date, K, optionType):
        _sigma = None
        if Global.VOLATILTY_MODE == 1:
            _sigma = Marketplace.getImpliedVolatility(creation_date)
        else:
            _sigma = Marketplace.getHistoricalVolatility(creation_date)
        _r = Marketplace.get_yield_for_date(current_date)
        bs = BlackScholes(_r, _sigma)
        st = Marketplace.getStockPriceOnDate(current_date)
        return bs.getRho(creation_date, current_date, expire_date, K, optionType, st)

    @staticmethod
    def get_yield_for_date(search_date):
        try:
            df = pd.read_csv(file_path)

            if 'date' not in df.columns or 'yield' not in df.columns:
                print("Column not found")
                return

            result = df[df['date'] == search_date]

            if not result.empty:
                yield_value = result.iloc[0]['yield']
                return yield_value
            else:
                print(f"No entry found {search_date}.")

        except FileNotFoundError:
            print(f"File not found: {file_path}.")
        except Exception as e:
            print(f"Error: {e}")

    @staticmethod
    def getMarketOptionGreeks(creation_date, current_date, expire_date, K, optionType):
        _sigma = None
        if Global.VOLATILTY_MODE == 1:
            _sigma = Marketplace.getImpliedVolatility(creation_date)
        else:
            _sigma = Marketplace.getHistoricalVolatility(creation_date)
        _r = Marketplace.get_yield_for_date(current_date)
        bs = BlackScholes(_r, _sigma)
        s0 = Marketplace.getStockPriceOnDate(creation_date)
        st = Marketplace.getStockPriceOnDate(current_date)
        return ([
            bs.getTheta(creation_date, current_date, expire_date, K, optionType, s0, st),
            bs.getGamma(creation_date, current_date, expire_date, K, optionType, s0, st),
            bs.getVega(creation_date, current_date, expire_date, K, optionType,s0, st),
            bs.getRho(creation_date, current_date, expire_date, K, optionType, st)
            ])

    @staticmethod
    def getMonteCarloPrice(creation_date, current_date, expire_date, K, optionType):
        mc = MonteCarlo()
        s0 = Marketplace.getStockPriceOnDate(creation_date)
        return mc.calcOptionPrice(creation_date, current_date, expire_date, K, optionType, s0)

    @staticmethod
    def getMonteCarloHedgingPricePairs(creation_date, current_date, expire_date, K, optionType, h):
        mc = MonteCarlo()
        s0 = Marketplace.getStockPriceOnDate(creation_date)
        return mc.calcHedgingPricePairs(creation_date, current_date, expire_date, K, optionType, s0, h)

    @staticmethod
    def getStockPriceOnDate(target_date):
        try:
            with open(file_path_stock, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    date = row.get('\ufeffStart')
                    if date == target_date:
                        high_price = float(row.get('High', 0))
                        low_price = float(row.get('Low', 0))
                        avg_price = (high_price + low_price) / 2
                        return avg_price

            print(f"Date {target_date} not found in the data.")
            return None 

        except FileNotFoundError:
            print(f"Could not find: {file_path_stock}")
        except Exception as e:
            print(f"Could not load data: {e}")

    @staticmethod
    def getOptionBigPhiA(creation_date, current_date, expire_date, K, optionType):
        _sigma = None
        if Global.VOLATILTY_MODE == 1:
            _sigma = Marketplace.getImpliedVolatility(creation_date)
        else:
            _sigma = Marketplace.getHistoricalVolatility(creation_date)
        _r = Marketplace.get_yield_for_date(current_date)
        bs = BlackScholes(_r, _sigma)
        st = Marketplace.getStockPriceOnDate(current_date)
        return bs.getBigPhiA(creation_date, current_date, expire_date, K, optionType, st)

    @staticmethod
    def getHistoricalVolatility(target_date):
        try:
            with open(file_path_volatility, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    date = row.get('Datum')
                    if date == target_date:
                        return float(row.get('Volatilität', 0)) + Global.VOLATILITY_PREMIUM

            print(f"Date {target_date} not found in the data.")
            return None 

        except FileNotFoundError:
            print(f"Could not find: {file_path_volatility}")
        except Exception as e:
            print(f"Could not load data: {e}")

    @staticmethod
    def getImpliedVolatility(search_date):
        if DateCalc.isDateBefore(search_date, "2023-03-24"):
            raise ValueError("No data before 2023-03-24 available!")
        try:
            df = pd.read_csv(file_path_implied_volatility)

            if 'Date' not in df.columns or 'DVOL' not in df.columns:
                print("Column not found")
                return

            result = df[df['Date'] == search_date]

            if not result.empty:
                vol = result.iloc[0]['DVOL']
                return vol * 0.01
            else:
                print(f"No entry found {search_date}.")

        except FileNotFoundError:
            print(f"File not found: {file_path_implied_volatility}.")
        except Exception as e:
            print(f"Error: {e}")



