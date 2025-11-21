"""
A manufacturer of metal pistons finds that,
on average, 12% of the pistons they manufacture are rejected
because they are incorrectly sized.
What is the probability that a batch of 10 pistons will contain:
 - No more than 2 rejects?
 - At least 2 rejects?
"""
import math

# Binomial coefficient (n/k) "n choose k" - number of B/G birth order patterns
# Evaluates to n! / (k! * (n - k)!). Added in version 3.8
c2o10 = math.comb(10, 2)  # 45
c8o10 = c2o10
c9o10 = 10

defect_rate = 12/100
nr = 1 - defect_rate
good8 = c8o10 * nr ** 8 * defect_rate ** 2  # 0.233
good9 = c9o10 * nr ** 9 * defect_rate       # 0.379
good10 = nr ** 10                           # 0.278

print(f'{good8 + good9 + good10:.3f}')  # 0.891
print(f'{1 - good9 - good10:.3f}')      # 0.342
