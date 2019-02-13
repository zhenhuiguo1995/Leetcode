def search( nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: int
	"""
	if not nums:
	    return -1
	start, end = 0, len(nums)-1
	
	while start +1 < end:
	    mid = (end - start)//2 + 1
	    if nums[mid] == target:
	        return mid
	    elif nums[mid] < target:
	        if nums[mid] > nums[0]:
	            start = mid
	        else:
	            end = mid
	    else:
	        if nums[mid] > nums[0]:
	            end = mid
	        else:
	            start = mid
	if nums[start] == target:
	    return start
	elif nums[end] == target:
	    return end
	else:
	    return -1
        
