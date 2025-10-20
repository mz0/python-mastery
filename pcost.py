def portfolio_cost(filename: str) -> float:
    val = 0.0
    with open(filename, 'r') as portf:
      for line in portf:
        r = line.split()
        try:
            q = int(r[1])
            p = float(r[2])
            print(f'{r[0]:7s} {q:>5d} @{p:>6.2f} makes {q * p:>6.2f}')
            val += q * p
        except ValueError as e:
            print(f'line "{r}" is bad ({e}) and is not counted')

    return val

if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))
