# Divide and conquer solution: assumes the definition of the recursion 
# has been implemented
# use recursion 

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # divide and conquer
        # definition 
        # given a root, returns the inverted tree rooted at the root
        def helper(root):
            # exit
            if root is None:
                return None

            # split
            left = helper(root.left)
            right = helper(root.right)
            root.left = right
            root.right = left
            return root
        
        helper(root)
        return root


"""
Iterative solution using stack and BFS
"""
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # iterative solution using BFS(level order)
        if root:    
            level = [root]
            while level:
                node = level.pop(0)
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)
        return root