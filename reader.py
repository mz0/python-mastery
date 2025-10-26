# reader.py

import csv


def convert_csv(lines_in, func, headers=None):
  rows = csv.reader(lines_in)
  if headers is None:
    headers = next(rows)
  return list(map(lambda row: func(row, headers), rows))


def csv_as_dicts(lines_in, types, *, headers=None):
  return convert_csv(lines_in,
                     lambda hds, row: {name: func(val) for name, func, val in zip(hds, types, row)},
                     headers=headers)


def csv_as_instances(lines_in, cls, *, headers=None):
  return convert_csv(lines_in,
                     lambda hds, row: cls.from_row(row),
                     headers=headers)

def read_csv_as_dicts(filename, types):
    """
    Read a CSV file into a list of dicts with column type conversion
    """
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    """
    Read a CSV file into a list of instances
    """
    with open(filename) as file:
      return read_csv_as_instances(file, cls)

def make_dict(hds, row):
    return dict(zip(hds, row))

if __name__ == "__main__":
  lines = open('Data/portfolio.csv')
  print(convert_csv(lines, make_dict))
