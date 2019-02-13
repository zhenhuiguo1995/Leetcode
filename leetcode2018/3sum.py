def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    array = []
    for i in range(len(nums)-2):
        if i == 0 or nums[i] != nums[i-1]:
            j, l = i+1, len(nums)-1
            while j < l:
                
                total = nums[i] + nums[j] + nums[l]
                print(total)
                if total == 0:
                    array.append([nums[i], nums[j], nums[l]])
                    while nums[j+1] == nums[j] and (j+1)<i:
                        j += 1
                    while nums[l] == nums[l-1] and (l-1)>j:
                        l -= 1
                    j, l = j+1, l-1
                elif total < 0:
                    while nums[j+1] == nums[j] and (j+1) < l:
                        j += 1
                    j += 1
                else:
                    while nums[l] == nums[l-1] and (l-1) > j:
                        l -= 1
                    l -= 1
        
    return array
nums = [-4,-1,-1,0, 1,2]
print(threeSum(nums))              