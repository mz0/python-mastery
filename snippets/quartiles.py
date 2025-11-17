#!/bin/env python3

def median(arr):
  N = len(arr)
  # m1, m2 - indices of median elements (or element when N is odd)
  if N % 2 == 0:
    m2 = N // 2
    m1 = m2 - 1
  else:
    m2 = N // 2
    m1 = m2
  return (arr[m1] + arr[m2]) / 2


def quartiles(arr):
    arr.sort()
    q2 = median(arr)
    h1 = [x for x in arr if x < q2]
    q1 = median(h1)
    h2 = [x for x in arr if x > q2]
    q3 = median(h2)
    return [int(q1), int(q2), int(q3)]


if __name__ == '__main__':
  data = [3, 7, 8, 5, 12, 14, 21, 13, 18, 10]
  res = quartiles(data)
  assert res == [7, 11, 14]
  print('\n'.join(map(str, res)))
