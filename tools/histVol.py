
import pandas as pd
from datetime import datetime, timedelta
import sys
import os
import math
import numpy as np

n = 30
csv_file = r"C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\data\Bitcoin2015_2024.csv"
output_csv = r"C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\bitcoin_volatility.csv"

def getDailyReturn(sDay, sDayBefore):
    return math.log(sDay/sDayBefore)

def calcStandardDeviation(date):
    array = get_last_n_days_close_values(date)
    new_array = [0] * n
    for i in range(n):
        new_array[i] = getDailyReturn(array[i], array[i+1])
    return np.std(new_array)

def getHistoricalVolatility(date):
    return calcStandardDeviation(date) * math.sqrt(365.2425)

def get_last_n_days_close_values(start_date):
    try:
        df = pd.read_csv(csv_file)
        df['timeOpen'] = pd.to_datetime(df['timeOpen'], format="%Y-%m-%dT%H:%M:%S.%fZ")
        start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_obj = start_date_obj
        start_date_n_days_ago = start_date_obj - timedelta(days=n+1)
        filtered_df = df[(df['timeOpen'] > start_date_n_days_ago) & (df['timeOpen'] <= end_date_obj)]
        close_values = filtered_df.sort_values(by='timeOpen', ascending=False)['close'].tolist()
        return close_values

    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return []

def save_volatility_to_csv(start_date, end_date, output_path):
    volatility_data = []
    
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    
    while current_date <= end_date_obj:
        date_str = current_date.strftime("%Y-%m-%d")
        
        try:
            volatility = getHistoricalVolatility(date_str)
            volatility_data.append([date_str, volatility])
        except Exception as e:
            print(f"Fehler bei der Berechnung der Volatilität für {date_str}: {e}")
        
        current_date += timedelta(days=1)
    
    df = pd.DataFrame(volatility_data, columns=["Datum", "Volatilität"])
    df.to_csv(output_path, index=False)
    print(f"Volatilität erfolgreich in {output_path} gespeichert.")

start_date = "2015-01-01"
end_date = "2024-12-15"
save_volatility_to_csv(start_date, end_date, output_csv)