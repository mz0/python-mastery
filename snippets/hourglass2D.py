#! /bin/env python3
from typing import List

def hgs(a: List, x: int, y:int) -> int:
  sum = 0
  seq3 = [0, 1, 2]
  for i in seq3:  # loop top->down
    for j in seq3:  # loop left->right
      if i == 1 and (j % 2 == 0):
        print(" ", end=" ")
        continue  # skip first and last in the middle row
      sum += a[x+i][y+j]
      print(a[x+i][y+j], end=" ")

    print('\n', end="")
  print(f'{sum}\n')
  return sum

if __name__ == '__main__':
  arr = []
  for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

  seq4 = [0, 1, 2, 3]
  mhgs = -10 * 36  # -10 < arr[i][j] < 10

  for i in seq4:
    for j in seq4:
      hs = hgs(arr, i, j)
      mhgs = hs if hs > mhgs else mhgs

  print(mhgs)
