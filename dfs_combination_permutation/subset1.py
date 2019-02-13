# a classical dfs with backtracking approach
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        # append each possible answer stored in res to result
        def helper(start, temp, ans):
            ans.append(temp.copy())
            
            for i in range(start, len(nums)):
                temp.append(nums[i])
                helper(i + 1, temp, ans)
                del temp[-1] # deleting the last element in a list
                
        helper(0, [], ans)
        return ans