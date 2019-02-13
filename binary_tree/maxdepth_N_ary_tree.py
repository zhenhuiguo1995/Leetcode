# BFS
# visit the tree layer by layer
# each time we enter a new layer, increase depth by 1
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root is not None:
            depth = 0
            level = [root]
            while level:
                depth += 1
                temp = []
                for node in level:
                    for child in node.children:
                        temp.append(child)
                level = temp
            return depth
        else:
            return 0


# Divide and conquer// also seems like a dfs way
# The max depth of the root = max(the depth of every node in root.children) + 1
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # divide and conquer
        def helper(root):
            depth = 0
            
            if root.children is None:
                return 1
            else:
                for child in root.children:
                    temp = helper(child)
                    if temp + 1 > depth:
                        depth = temp + 1
                return depth + 1
            
        if root is not None:
            return helper(root) + 1
        else:
            return 0
    
# DFS quite similiar to divide and conquer
# the basic idea behind the two approach are the same
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        # definition: returns the depth of the given node
        def dfs(root):
            # exit
            if root.children is None:
                return 1
            
            # split
            depth = 0
            for child in root.children:
                depth = max(depth, dfs(child))
            return depth + 1    
            
        if root is not None:
            return dfs(root)
        else:
            return 0
            