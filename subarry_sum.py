def subarry_sum(nums, k):
    d = {0: 1}
    total = 0
    count =0

    for x in nums:
        total += x

        if total - k in d:
            count += d[total - k]
        if total in d:
            d[total] += 1
        else:
            d[total] = 1

    return count

print(subarry_sum([3,4,7,2,-3,1,2,4], 7))