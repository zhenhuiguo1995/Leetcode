# divide and conquer way
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_diameter = 0
        
        # definition: returns the max depth of the node
        def max_depth(node):
            nonlocal max_diameter
            # exit
            if node is None:
                return 0
            # split
            else:
                left = max_depth(node.left)
                right = max_depth(node.right)
                max_diameter = max(max_diameter, left + right)
                return max(left, right) + 1
            
        max_depth(root)
        return max_diameter