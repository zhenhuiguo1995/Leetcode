# a divide and conquer way
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # definiton, return a boolean(balanced), and the height of the subtree
        def helper(root):
            # exit
            if root is None:
                return True, 0
            
            # split
            else:
                left, l_height = helper(root.left)
                right, r_height = helper(root.right)
                return (abs(l_height - r_height) <= 1) and left and right, max(l_height, r_height) + 1
        
        return helper(root)[0]