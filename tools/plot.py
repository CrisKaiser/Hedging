import pandas as pd
import matplotlib.pyplot as plt

dvol_df = pd.read_csv(r'data\dvol_data.csv', parse_dates=['Date'])
interest_df = pd.read_csv(r'data\bitcoin_volatility.csv', parse_dates=['Datum'])

start_date = '2023-03-24'
end_date = '2024-12-10'

dvol_df = dvol_df[(dvol_df['Date'] >= start_date) & (dvol_df['Date'] <= end_date)]
interest_df = interest_df[(interest_df['Datum'] >= start_date) & (interest_df['Datum'] <= end_date)]

dvol_df['DVOL'] = dvol_df['DVOL'] / 100

dvol_df = dvol_df.rename(columns={'Date': 'Datum'})

merged_df = pd.merge(dvol_df, interest_df, on='Datum', how='inner')

plt.figure(figsize=(10, 6))

plt.plot(merged_df['Datum'], merged_df['DVOL'], label='DVOL', color='blue')
plt.plot(merged_df['Datum'], merged_df['Volatilität'], label='Historical Volatility', color='red')

plt.xlabel('Date')
plt.ylabel('Per cent')
plt.title('DVOL versus Historical Volatility')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Diagramm anzeigen
plt.show()
