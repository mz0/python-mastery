import sys
from collections import Counter

aaa = "abcdefghijklmnopqrstuvwxyz"
e = aaa[::2]
o = aaa[1::2]
print(e, o, len(aaa))

# xsum = 23
# N = len(aaa)
# print(f'{xsum/N:.1f}\n')
N = 9  # int(sys.stdin.readline().strip())
if N % 2 == 0:
    m2 = N // 2
    m1 = m2 - 1
else:
    m2 = 1 + N // 2
    m1 = m2

print(N, m1, m2)

case1 = "64630 11735 14216 99233 14470 4978 73429 38120 51135"
X = list(map(int, case1.strip().split()))
X.sort()
if not N == len(X): print(f'N={N}')
print(X)
print(X[m1], X[m2])

xsum = sum(X)
mc, _ = Counter(X).most_common(1)[0]
median = (X[m1] + X[m2]) / 2
print(f'{xsum/N:.1f}')  # mean
print(f'{median:.1f}')
print(mc)
