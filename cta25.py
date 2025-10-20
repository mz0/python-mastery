import csv
# Read as columns
def read_rides_as_columns(filename):
    """
    Read the bus ride data into 4 lists, representing columns
    """
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    read_rides = read_rides_as_columns
    rides = read_rides("Data/ctabus.csv")

    current, peak = tracemalloc.get_traced_memory()
    print(f'Memory Use (Bytes): Current {current:,d}, Peak {peak:,d}')
# Current 87,209,486, Peak 87,239,976
