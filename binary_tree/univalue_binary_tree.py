"""
Definition:
A binary tree is univalued if every node in the tree has the same value.
Return true if and only if the given tree is univalued.
"""
# Iteratice way with BFS (using queue)
# Set the root as a default value and compares every node in the tree
# with the default value until a different value is met or all nodes have the 
# same vaue
class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            value = root.val
            queue = [root]
            while queue:
                curr = queue.pop(0)
                if curr.val != value:
                    return False
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return True


# Recursive way (Mmore of DFS)
class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(root):
            if not root:
                return True
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False
            return helper(root.left) and helper(root.right)
        return helper(root)