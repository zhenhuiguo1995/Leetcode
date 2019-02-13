def thirdMax(nums):
    """
    find the third largest element in an array
    """
    if len(set(nums)) < 3:
        return max(nums)
    else:
        nums = list(set(nums))
        nums.sort()
    return nums[len(nums)-3]


    """
    another solution is to find the largest, second-largest, and 
    third-largest element of the array, respectively
    """