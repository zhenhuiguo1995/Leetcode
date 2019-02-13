# a divide and conquer way
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # recursion
        # return a TreeNode rooted at the middle of nums
        def helper(nums):
            # exit
            if not nums: # when nums is empty
                return None
            # split
            middle = len(nums)//2
            root = TreeNode(nums[middle]) # TreeNode is predefined
            root.left = helper(nums[:middle]) 
            root.right = helper(nums[middle + 1:])
            return root
        return helper(nums)