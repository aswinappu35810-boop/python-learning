def maskAllButLastFour(digits):
    result = ""
    limit = len(digits)-5
    if len(digits)<=4:
        return digits
    for i in range(0, len(digits)):
        if i <= limit:
            result = result + "*"
        else:
            result = result + digits[i]
    return result
