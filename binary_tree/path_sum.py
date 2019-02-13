# DFS way
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # definition: total = sum of every node in this path
        def dfs(root, total):
            # exit
            if root.left is None and root.right is None:
                if total + root.val == sum:
                    return True
                else:
                    return False
            # split -> how to discuss the problem
            else:
                if root.right is None:
                    return dfs(root.left, total + root.val)
                if root.left is None:
                    return dfs(root.right, total + root.val)
                else:
                    return dfs(root.left, total + root.val) or dfs(root.right, total + root.val)
        
        if root:
            return dfs(root, 0)    
        return False