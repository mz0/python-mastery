#!/bin/env python3

def weightedMean(X, W):
  weighted = sum([x * w for x,w in zip(X, W)])
  wm = weighted / sum(W)
  print(f'{wm:.1f}')
  return wm


if __name__ == '__main__':
    vals = [11, 40, 30, 50, 20]
    weights = [11, 2, 3, 4, 5]
    assert weightedMean(vals, weights)  == 23.64
