"""
The ratio of boys to girls for babies born in Russia is 1.09:1
If there is 1 child born per birth, what proportion of Russian families
with exactly 6 children will have at least 3 boys?
"""
bp = 109/209
gp = 1 - bp
# Binomial coefficient (n/k) "n choose k" - number of B-G birth order patterns
pb3 = 20 * bp ** 3 * gp ** 3  # 0.31
pb4 = 15 * bp ** 4 * gp ** 2  # 0.254
pb5 =  6 * bp ** 5 * gp ** 1  # 0.11
pb6 =      bp ** 6            # 0.02
print(f'{pb3 + pb4 + pb5 + pb6:.3f}')  # 0.696
