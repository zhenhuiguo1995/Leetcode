class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(start, path, res):
            res.append(path.copy())# you have to make a copy of the original list

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: # skip the same items
                    continue
                path.append(nums[i])
                helper(i + 1, path, res)
                del path[-1] # first append then remove 
        
        
        res = []
        nums.sort()
        helper(0, [], res)
        return res
    
