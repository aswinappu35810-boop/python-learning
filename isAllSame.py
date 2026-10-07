def isAllSame(items):
    if len(items) == 0:
       return True
    for i in range(1, len(items)):
        if items[i]!= items[0]:
            return False
    return True
