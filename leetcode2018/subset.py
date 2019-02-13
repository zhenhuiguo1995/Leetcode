def subset(nums):
    res = [[]]
    for num in nums:
        res += [i + [num] for i in res]
    return res'