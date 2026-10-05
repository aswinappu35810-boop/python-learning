def alternatingSum(numbers):
    result = 0
    for i, x in enumerate(numbers):
        # print(i, x)
        if i % 2 == 0:
            result += x
        else:
            result -= x
    return result
                
