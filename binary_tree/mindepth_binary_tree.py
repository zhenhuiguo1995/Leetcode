class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # use a "bfs" approach -> visit nodes layer by layer
        # if we encounter a node which has no left and right nodes, then we 
        # return its layer index, otherwise we add its existing children into
        # the next layer's list
        def helper(nodes, i):
            temp = []
            for node in nodes:
                if node.left is None and node.right is None:
                    return i
                else:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
            return helper(temp, i + 1)        
        
        if root:
            return helper([root], 1)
        else:
            return 0