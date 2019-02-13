# level order traversal of a binary tree
# essentially, level order of a tree can be conducted by a bfs
def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root:
        stack = [root]
        res = []
        while stack:
            res.append([node.val for node in stack])
            children = []
            for node in stack:
                if node.left:
                    children.append(node.left)
                if node.right:
                    children.append(node.right)
            stack = children
        return res
    return []     

        