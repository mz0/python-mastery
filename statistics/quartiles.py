#!/bin/env python3

def median(arr):
  arr_len = len(arr)
  if arr_len % 2 == 0:
    # m1, m2 - indices of median elements
    m2 = arr_len // 2
    print(f'Even; m2={m2}')
    m1 = m2 - 1
    return (arr[m1] + arr[m2]) / 2, m1, m2
  else: # m2 - median element index (when arr_len is odd)
    m2 = arr_len // 2
    print(f'Odd; m2={m2}')
    return arr[m2], m2, m2


def quartiles(arr):
    arr.sort()
    q2, _, _ = median(arr)
    h1 = [x for x in arr if x < q2]
    q1, _, _ = median(h1)
    h2 = [x for x in arr if x > q2]
    q3, _, _ = median(h2)
    return [int(q1), int(q2), int(q3)]


def interQuartile(values, freqs):
  sorted_pairs = sorted(zip(values, freqs))
  S = [v for v, f in sorted_pairs for _ in range(f)]
  q2, m1, m2 = median(S)
  mi = m2 + 1 if m2 == m1 else m2
  q1, _, _ = median(S[:m2])
  q3, _, _ = median(S[mi:])
  iq = q3 - q1
  print(f'Length: {len(S)}; inter-quartile: {iq:.1f}')

if __name__ == '__main__':
  data = [3, 7, 8, 5, 12, 14, 21, 13, 18, 10]
  res = quartiles(data)
  assert res == [7, 11, 14]
  print('\n'.join(map(str, res)))

  # val = [6, 12, 8, 10, 20, 16]
  # frq = [5, 4, 3, 2, 1, 5]
  # interQuartile(val, frq)

  val = [10,40,30,50,20,10,40,30,50,20,1,2,3,4,5,6,7,8,9,10]
  frq = [1,2,3,4,5,6,7,8,9,10,10,40,30,50,20,10,40,30,50,20]
  print(f'Expected S length: {sum(frq)}')
  interQuartile(val, frq)
