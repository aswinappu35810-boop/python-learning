def countItemsAbove(numbers, limit):
    count = 0
    for i in range(len(numbers)):
        if numbers[i]>=limit:
            count = count + 1
        
    return count
