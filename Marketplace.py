import pandas as pd
from BlackScholes import BlackScholes; 

file_path = "data\interest_rates.csv"

def getMarketOptionPrice(creation_date, current_date, expire_date, K, optionType):
    _sigma = 0.1 #to be complited

    _r = get_yield_for_date(file_path, current_date)

    bs = BlackScholes(_r, _sigma)
    return bs.calcOptionPrice(creation_date, current_date, expire_date, K, optionType)

def get_yield_for_date(file_path, search_date):
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