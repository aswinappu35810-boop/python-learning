def pairUpTwoLists(first, second):
    result = []
    for x, y in zip(first, second):
        result.append([x, y])
    return result
