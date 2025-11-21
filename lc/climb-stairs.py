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
    fib45 = [0] * 46  # 17.86 MB Beats 29.86%

    def __init__(self):
      self.fib45[1] = 1
      self.fib45[2] = 2
      for i in range(3, 46):
        self.fib45[i] = self.fib45[i - 2] + self.fib45[i - 1]

    def climbStairs(self, n: int) -> int:
      if n == 1:
        return 1
      elif n == 2:
        return 2
      else:
        n_1th = 2
        n_2th = 1
        i = 2
        result = 0
        while i < n:
          result = n_1th + n_2th
          i += 1
          n_2th = n_1th
          n_1th = result

        return result


if __name__ == '__main__':
  sol = Solution()
  print(sol.climbStairs(4))
  print(sol.climbStairs(5))
  print(sol.climbStairs(6))
  print(sol.climbStairs(45))
