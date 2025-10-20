import tracemalloc
import csv

tracemalloc.start()

f = open('Data/ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)
rows = (dict(zip(headers,row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
print(max(rt22, key=lambda row: int(row['rides'])))
# {'route': '22', 'date': '06/11/2008', 'daytype': 'W', 'rides': '26896'}

current, peak = tracemalloc.get_traced_memory()
print(f'Memory Use (Bytes): Current {current:,d}, Peak {peak:,d}')
# Current 27,628, Peak 45,097
