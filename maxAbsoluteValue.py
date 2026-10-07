def maxAbsoluteValue(numbers):
    max = 0
    for i in range(len(numbers)):
        if abs(numbers[i])>max:
            max = abs(numbers[i])
    return max
            
