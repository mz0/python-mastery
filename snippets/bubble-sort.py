a = [4, 3, 1, 2]
allswaps = 0
for i in range(len(a)):
  swaps = 0
  for j in range(i+1, len(a)):
    if a[j] < a[i]:
      t = a[i]
      a[i] = a[j]
      a[j] = t
      swaps += 1

  allswaps += swaps
  if swaps == 0: break

print(a)
print(allswaps)
