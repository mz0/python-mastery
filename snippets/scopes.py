class Difference:
  def __init__(self, a):
    self.__elements = a
    self.__elements.sort()

  def computeDifference(self):
    self.maximumDifference = abs(self.__elements[0] - self.__elements[-1])


a = [11, 100, 2, 3, 5, 21, 1]
d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
