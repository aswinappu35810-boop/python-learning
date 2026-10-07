def roundToTwoDecimals(numbers):
    result = []
    for i in range(len(numbers)):
        
         result.append(round(numbers[i], 2))
    return result