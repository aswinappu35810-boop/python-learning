def largestValueKey(scores):
    largest = float("-inf")
    res = ""
    for key,value in scores.items():
        if largest<value:
            largest = value 
            res = key
    return res