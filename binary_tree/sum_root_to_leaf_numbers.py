# DFS recursive version
# use an additional parameter path_sum to record the sum of the path so far
# return the sum of the path value when the leaf node is met
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # definition
        # given a root and the path value
        # increase the path value whenever still on the path
        # returns the pathsum of the current path
        
        def dfs(root, path_sum):
            # exit a.k.a. base case
            if root.left is None and root.right is None:
                return path_sum * 10 + root.val
            # split
            else:
                if root.right is None:
                    return dfs(root.left, path_sum * 10 + root.val)
                if root.left is None:
                    return dfs(root.right, path_sum * 10 + root.val)
                else:
                    return dfs(root.left, path_sum * 10 + root.val) + dfs(root.right, path_sum * 10 + root.val)
        
        if root:
            return dfs(root, 0)
        else:
            return 0

# DFS with stack solution
# use a tuple in the stack (x, y) where x is the node and y are the sum of 
# path before we met x
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # DFS with stack
        if root:
            stack = [(root, 0)]
            total = 0
            while stack:
                node, value = stack.pop(0)
                if node.left is None and node.right is None:
                    total += value * 10 + node.val
                elif node.right is None:
                    stack.append((node.left, value * 10 + node.val))
                elif node.left is None:
                    stack.append((node.right, value * 10 + node.val))
                else:
                    stack.append((node.left, value * 10 + node.val))
                    stack.append((node.right, value * 10 + node.val))
            return total
        else:
            return 0