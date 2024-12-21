import csv
from datetime import datetime, timedelta

# Definiere die Zinsänderungsdaten und -werte
changes = [
    ("2009-05-07", 0.01),
    ("2011-04-07", 0.0125),
    ("2011-07-07", 0.015),
    ("2011-11-03", 0.0125),
    ("2011-12-08", 0.01),
    ("2012-07-05", 0.0075),
    ("2013-05-02", 0.005),
    ("2013-11-07", 0.0025),
    ("2014-06-05", 0.0015),
    ("2014-09-04", 0.0005),
    ("2016-03-10", 0.0),
    ("2022-07-21", 0.005),
    ("2022-09-08", 0.0125),
    ("2022-10-27", 0.02),
    ("2022-12-15", 0.025),
    ("2023-02-02", 0.03),
    ("2023-03-16", 0.035),
    ("2023-05-04", 0.0375),
    ("2023-06-15", 0.04),
    ("2023-07-27", 0.0425),
    ("2023-09-14", 0.045),
    ("2024-06-06", 0.0425),
    ("2024-09-12", 0.0365),
    ("2024-10-17", 0.034),
    ("2024-12-12", 0.0315)
]

# Konvertiere Datumsstrings in datetime-Objekte
changes = [(datetime.strptime(date, '%Y-%m-%d'), yield_) for date, yield_ in changes]

# Zeitraum definieren
start_date = datetime.strptime("2010-07-17", '%Y-%m-%d')
end_date = datetime.strptime("2024-12-15", '%Y-%m-%d')

# Pfad zur Datei festlegen
file_path = 'interest_rates.csv'

# CSV-Datei erstellen
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['date', 'yield'])

    current_yield = None
    change_index = 0

    # Initialisiere current_yield auf den ersten Zinswert vor dem Startdatum
    for i in range(len(changes)):
        if changes[i][0] <= start_date:
            current_yield = changes[i][1]
        else:
            change_index = i
            break

    # Für jeden Tag im definierten Zeitraum
    current_date = start_date
    while current_date <= end_date:
        # Überprüfen, ob ein Zinsänderungstag erreicht ist
        if change_index < len(changes) and current_date == changes[change_index][0]:
            current_yield = changes[change_index][1]
            change_index += 1

        # Manuelles Formatieren des Datums ohne führende Nullen
        date_str = f"{current_date.year}-{current_date.month}-{current_date.day}"
        writer.writerow([date_str, current_yield])

        current_date += timedelta(days=1)
