import csv
from collections.abc import Sequence


class RideData(Sequence):
    def __init__(self):
        # Each value is a list with all the values (a column)
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        # All lists assumed to have the same length
        return len(self.routes)

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])

    def __getitem__(self, index):
        return {'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]}


# Modified version using RideData
def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of dicts
    """
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rs = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rs
            }
            records.append(record)
    return records


if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    read_rides = read_rides_as_dicts
    rides = read_rides("Data/ctabus.csv")

    current, peak = tracemalloc.get_traced_memory()
    print(f'Memory Use (Bytes): Current {current:,d}, Peak {peak:,d}')
# Current 87,209,734, Peak 87,240,288
