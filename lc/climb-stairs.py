#! /bin/env python3
"""
70.
https://leetcode.com/problems/climbing-stairs

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?
Constraints: 1 <= n <= 45
"""

class Solution:
    fib45 = []  # 17.62 MB Beats 78.08%

    def __init__(self, n_max):
      self.fib45 = list(self.fibonacci_generator(n_max))

    @staticmethod
    def fibonacci_generator(m):
      a, b = 1, 2
      for _ in range(m):
        yield a
        a, b = b, a + b

    def climb12(self, n: int) -> int:
      return self.fib45[n - 1]


if __name__ == '__main__':
  sol = Solution(45)
  assert sol.climb12(5) == 8
  assert sol.climb12(6) == 13
  assert sol.climb12(45) == 1836311903
  print(sol.climb12(45))
