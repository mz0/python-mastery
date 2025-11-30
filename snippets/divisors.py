#!/bin/env python3

def divisorSum(n):
  divisors = [1]
  d = 2
  while d <= n:
      if n % d == 0:
          divisors.append(d)
      d += 1
  return sum(divisors)

print(divisorSum(20))
