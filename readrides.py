# readrides.py

import csv
from reader import read_csv_as

# Memory Use (Bytes): Current 179,414,046, Peak 179,427,882
# def read_rides_as_dict(filename):
#     records = []
#
#     with open(filename, 'r') as f:
#         next(f)  # skip headers
#         line_count = 1
#         for line in f:
#             line_count += 1
#             r = line.split(',')
#             try:
#                 route = r[0]  # e.g. "8A", "81W", "N201"
#                 date = r[1]
#                 dt = r[2]
#                 rides = int(r[3])
#                 row = {'route': route, 'date': date, 'daytype': dt, 'rides': rides,}
#                 records.append(row)
#             except ValueError:
#                 print(f'Line {line_count:5d}: "{line}" is malformed')
#     return records

# A named tuple
# from collections import namedtuple
# Row = namedtuple('Row', ['route', 'date', 'daytype', 'rides'])

# A class with __slots__
class Row:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, day_type, rides):
        self.route = route
        self.date = date
        self.daytype = day_type
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# csv, reader, _as  Memory Use (Bytes): Current 110,109,311, Peak 110,139,584
# Class with slots: Memory Use (Bytes): Current 110,108,910, Peak 110,122,746
def read_rides_as_class(filename):
    records = []

    with open(filename, 'r') as f:
        next(f)  # skip headers
        line_count = 1
        for line in f:
            line_count += 1
            r = line.split(',')
            try:
                route = r[0]  # e.g. "8A", "81W", "N201"
                date = r[1]
                dt = r[2]
                rides = int(r[3])
                records.append(Row(route, date, dt, rides))
            except ValueError:
                print(f'Line {line_count:5d}: "{line}" is malformed')
    return records

# Named Tuples: Memory Use (Bytes): Current 119,350,118, Peak 119,363,954
# def read_rides_nt(filename):
#     records = []
#     with open(filename, 'r') as f:
#         next(f)  # skip headers
#         line_count = 1
#         for line in f:
#             line_count += 1
#             r = line.split(',')
#             try:
#                 route = r[0]  # e.g. "8A", "81W", "N201"
#                 date = r[1]
#                 dt = r[2]
#                 rides = int(r[3])
#                 records.append(Row(route, date, dt, rides))
#             except ValueError:
#                 print(f'Line {line_count:5d}: "{line}" is malformed')
#     return records

# Memory Use (Bytes): Current 114,729,038, Peak 114,759,528
# Memory Use (Bytes): Current 114,728,982, Peak 114,742,818 - no csv, int(rides)
# Memory Use (Bytes): Current 125,882,392, Peak 125,896,183 - no csv
def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows_iter = csv.reader(f)
        next(rows_iter)
        for row in rows_iter:
            route = row[0]
            date = row[1]
            day_type = row[2]
            rides = int(row[3])
            record = (route, date, day_type, rides)
            records.append(record)
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_csv_as('Data/ctabus.csv', Row)
    current, peak = tracemalloc.get_traced_memory()
    print(f'Memory Use (Bytes): Current {current:,}, Peak {peak:,}')
