def powersOfTwoUpTo(limit):
    result = []
    x = 1
    for i in range(limit):
        if x<=limit:
            result.append(x)
            x *= 2
    return result