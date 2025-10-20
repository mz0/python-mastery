import tracemalloc
from collections import defaultdict, Counter
import readrides


tracemalloc.start()

rows = readrides.read_rides_as_class('Data/ctabus.csv')
buses = {r.route for r in rows}
# len(buses) 181
# buses {'94', '21', 'X20', .. '90N', 'N201', '81W', '69BR', 'X99'}

# --------------------------------------------------
# Question 2: How many people rode route 22 on February 2, 2011?
# not using dictionary with composite keys: by_route_date[row['route'], row['date']] = ...)
r22feb2 = [r for r in rows if r.route == '22' and r.date == '02/02/2011']
if r22feb2: print('Route 22:', r22feb2[0].rides)

by_route_date = { }
for row in rows:
    by_route_date[row.route, row.date] = row.rides

print('Rides on Route 22, February 2, 2011:', by_route_date['22','02/02/2011'])

# --------------------------------------------------
# Question 3: Total number of rides per route
rides_per_route = Counter()
for route, cnt in rides_per_route.most_common():  # print all 181 lines sorted
  print('%5s %10d' % (route, cnt))

# --------------------------------------------------
# Question 4: Routes with greatest increase in ridership 2001 - 2011
rides_by_year = defaultdict(Counter)
for r in rows:
  y = r.date.split('/')[2]
  rides_by_year[y][r.route] += r.rides

diffs = rides_by_year['2011'] - rides_by_year['2001']
for route, diff in diffs.most_common(5):
  print(route, diff)

current, peak = tracemalloc.get_traced_memory()
print(f'Memory Use (Bytes): Current {current:,d}, Peak {peak:,d}')