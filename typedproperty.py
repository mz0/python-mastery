class TypedProperty:
  """
  A descriptor that enforces a specific type for a property.
  It uses __set_name__ to automatically get the attribute name.
  """

  def __init__(self, expected_type):
    self.expected_type = expected_type
    self.private_name = None

  def __set_name__(self, cls, name):
    # This is called when the descriptor is assigned to an attribute.
    # 'name' is the name of the attribute (e.g., 'shares').
    self.private_name = '_' + name

  def __get__(self, instance, cls):
    if instance is None:
      return self
    if self.private_name is None:
      raise AttributeError("TypedProperty was not correctly initialized.")
    return getattr(instance, self.private_name)

  def __set__(self, instance, value):
    if self.private_name is None:
      raise AttributeError("TypedProperty was not correctly initialized.")
    if not isinstance(value, self.expected_type):
      raise TypeError(f'[ {value} ] is not a {self.expected_type}')
    setattr(instance, self.private_name, value)


# Type-specific descriptor factories
def String(): return TypedProperty(str)
def Integer(): return TypedProperty(int)
def Float(): return TypedProperty(float)

class Stock:
    name = String()
    shares = Integer()  # TypedProperty.__set_name__(self, Stock, 'shares')
    price = Float()

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('GOOG', 10, 44.22)
    print(repr(s))

    try:
      s.shares = 2.5
    except TypeError as e:
      print(f"s.shares = 2.5 - Error as expected: {e}")

    # private name is handled correctly
    print(f"Internal storage: s._shares = {s._shares}, s._price = {s._price}")
