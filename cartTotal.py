def cartTotal(prices, quantities):
    total = 0
    for x,y in zip(prices, quantities):
        total += x*y
    return total
