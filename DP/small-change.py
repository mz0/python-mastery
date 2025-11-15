#!/bin/env python3

def get_ways(n, c):
  c.sort()
  memo = {}

  def count(amount, idx):
    """
    Returns the number of ways to make 'amount'
    using coins up to c[index].
    """
    if (amount, idx) in memo:
      return memo[(amount, idx)]

    if amount == 0: return 1  # perfect match
    if amount < 0 or idx < 0: return 0  # Overshot the amount, or ran out of coin options

    # Two Choices
    no_ith_coin = count(amount, idx - 1)  # not using the "current" coin, use the next smaller one
    using_coin = count(amount - c[idx], idx)  # use it (at least) once
    ways = no_ith_coin + using_coin
    memo[(amount, idx)] = ways
    return ways

  return count(n, len(c) - 1)


if __name__ == '__main__':
  coins = [7, 1, 3, 2]
  am = 3
  print(f'For amount of {am} change can be made in {get_ways(am, coins)} ways using coins {coins}')
