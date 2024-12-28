import requests
import csv

url = "https://www.deribit.com/api/v2/public/get_delivery_prices"

def fetch_dvol_for_index(index_name):
    results = []
    offset = 0
    count = 100 
    while True:
        try:
            params = {'index_name': index_name, 'offset': offset, 'count': count}
            response = requests.get(url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                if 'result' in data and 'data' in data['result']:
                    batch = data['result']['data']
                    if not batch: 
                        break
                    results.extend([(entry['date'], entry['delivery_price']) for entry in batch])
                    offset += count  
                    print(f"{index_name} - Ältestes Datum bisher: {batch[-1]['date']}")
                else:
                    print(f"{index_name} - Keine weiteren Ergebnisse.")
                    break
            else:
                print(f"{index_name} - Fehler: {response.status_code}")
                break
        except Exception as e:
            print(f"{index_name} - Fehler beim Abrufen: {e}")
            break
    return results

def write_to_csv(data, filename="dvol_data.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "DVOL", "Index"])
        writer.writerows(data)

def main():
    index_names = ['btcdvol_usdc', 'BTCDVOL_USDC-DERIBIT-INDEX', 'BTC-DVOL']
    all_results = []
    
    for index_name in index_names:
        print(f"Rufe Daten für Index: {index_name} ab...")
        results = fetch_dvol_for_index(index_name)
        if results:
            all_results.extend([(date, price, index_name) for date, price in results])
    
    if all_results:
        write_to_csv(all_results)
        print(f"DVOL-Daten gespeichert: {len(all_results)} Einträge.")
    else:
        print("Keine Daten verfügbar.")

if __name__ == "__main__":
    main()
