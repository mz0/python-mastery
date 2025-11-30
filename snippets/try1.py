#!/bin/env python3

class Calculator:
  def power(self, e, exponent):
    if e < 0 or exponent < 0:
      raise ValueError('n and p should be non-negative')
    return e ** exponent

if __name__ == '__main__':
    S = input()
    try:
        print(int(S))
    except ValueError:
        print('Bad String')


    myCalculator = Calculator()
    try:
      ans = myCalculator.power(2, 5)
      print(ans)
    except Exception as e:
      print(e)
