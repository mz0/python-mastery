#! /bin/env python3
# g(n, p) = q^(n-1) * p
# p - success probability, n - number of experiments, q = 1 - p

"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect occurs the 5th item produced?
"""
p = 1 / 3
q = 1 - p
g_5_p = (q ** 4) * p
answer1 = f'{g_5_p:.3f}'
assert  answer1 == '0.066'

"""
The probability that a machine produces a defective product is 1/3.
What is the probability that the  defect is found
during the first 5 inspections?
"""
p = 1 / 3
q = 1 - p
p1 = p
p2 = q * p
p3 = q * q * p
p4 = q * q * q * p
p5 = q * q * q * q * p
answer5 = f'{p1 + p2 + p3 + p4 + p5:.3f}'
assert answer5 == '0.868'
