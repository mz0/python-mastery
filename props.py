class Stock:
  def __init__(self, name, shares, price):
    self._name = name
    self._shares = shares
    self.price = price

  @property
  def shares(self):
    return self._shares

  @shares.setter
  def shares(self, value):
    if not isinstance(value, int):
       raise TypeError('Expected int')
    self._shares = value


ii = Stock('INTC', 100, 32.20)
ii.shares  # 100
ii.shares = 120
ii.shares  # 120
