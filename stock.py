from decimal import Decimal

class Stock:
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = non_negative_int(shares)
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = non_negative_int(value)

    @property
    def cost(self):
        return round(self.shares * self.price, 2)

    def sell(self, qty):
        self.shares -= qty

    @classmethod
    def from_row(cls, row):
        vals = [f(val) for f, val in zip(cls._types, row)]
        return cls(*vals)

def non_negative_int(val):
    if not isinstance(val, int) or val < 0:
        raise TypeError('Expected int >= 0')
    return val

class DStock(Stock):
    types = (str, int, Decimal)


def read_portfolio(filename):
    portf = list()
    with open(filename) as f:
        f.readline()  # skip headers
        for line in f:
            r = line.split(',')
            portf.append(Stock(r[0].strip('"'), int(r[1]), float(r[2])))
    return portf

if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
