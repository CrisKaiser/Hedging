import pandas as pd
import matplotlib.pyplot as plt

#csv_files = [r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\CONS_IV_DI.csv', r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\Flex_IV_DI.csv', r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\Simple_IV_DI.csv']  # Ersetze durch den tatsächlichen Pfad der CSV-Dateien
#csv_files = [r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\CONS_HV_DI.csv', r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\FLEX_HV_DI.csv', r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\Simple_HV_DI.csv']
csv_files = [r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\CONS_HV.csv', r'C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\FLEX_HV.csv', r"C:\Users\crisk\Documents\uni\Semester3\ModSim\Pricing\code\sim\Simple_HV.csv"]
data_frames = []
labels = ['Conservative', 'Flex', 'Naive']  


for file in csv_files:
    df = pd.read_csv(file)
    df['Date'] = pd.to_datetime(df['Date'])  
    data_frames.append(df)

plt.figure(figsize=(10, 6))

for i, df in enumerate(data_frames):
    plt.plot(df['Date'], df['Equity'], label=labels[i])

plt.title('Equity Kursverläufe über die Zeit')
plt.xlabel('Datum')
plt.ylabel('Equity')
plt.legend()

plt.xticks(rotation=45) 
plt.tight_layout()  
plt.show()
