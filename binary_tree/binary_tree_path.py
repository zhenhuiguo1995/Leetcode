# DFS recursive solution
# traverse through the tree
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        # definition
        # given root(the node to be traversed)
        # path(the path from tree root to the node before current root)
        def dfs(root, path):
            # exit: when root is a leaf node
            if root.left is None and root.right is None:
                result.append(path)
            
            # split:
            else:
                if root.left:
                    dfs(root.left, path + "->" + str(root.left.val))
                if root.right:
                    dfs(root.right, path + "->" + str(root.right.val))
                
        if root:
            dfs(root, str(root.val))
        return result


# DFS with stack
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right: # deals with leaf node
                res.append(path + str(node.val))
            if node.right:
                stack.append((node.right, path + str(node.val)+"->"))
            if node.left:
                stack.append((node.left, path + str(node.val)+"->"))
        return res
