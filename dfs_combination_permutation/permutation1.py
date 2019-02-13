# dfs solution 
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(path, ans):
            if len(path) == len(nums):
                ans.append(path.copy())
            else:
                for i in range(len(nums)):
                    if nums[i] in path:
                        continue
                    else:
                        path.append(nums[i])
                        helper(path, ans)
                        del path[-1]
        
        
        ans = []
        helper([], ans)
        return ans