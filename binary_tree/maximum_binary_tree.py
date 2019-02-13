# classical divide and conquer solution
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # divide and conquer
        def helper(nums):
            # base case
            if not nums:
                return None
            
            # exit
            temp = max(nums)
            root = TreeNode(temp)
            index = nums.index(temp)
            root.left = helper(nums[:index])
            root.right = helper(nums[index+1:])
            return root
        return helper(nums)