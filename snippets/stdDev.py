#!/bin/env python3
from math import sqrt

def stdDev(arr):
  mean = sum(arr) / len(arr)
  dsq = sum([(x - mean) ** 2 for x in arr]) / len(arr)
  print(f'{sqrt(dsq):.1f}')


if __name__ == '__main__':
  vals = [10, 40, 30, 50, 20]
  stdDev(vals)
