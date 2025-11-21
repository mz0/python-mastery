#! /bin/env python3

if __name__ == '__main__':
  n = int(input().strip())
  n_as_bits = f'{n:b}'
  max1 = 0
  cont1 = 0

  for digit in n_as_bits:
    if digit == '1':
      cont1 += 1
      if cont1 > max1: max1 = cont1
    else:
      cont1 = 0

  print(max1)

# hackerrank 3.13.3 (main, May 21 2025, 23:33:29) [GCC 10.2.1 20210110]
