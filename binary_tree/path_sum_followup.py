# still DFS
# add a variable path in dfs which records the path from the actuall root to
# the current node 
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        # definition:
        def dfs(root, path, total):
            # exit a.k.a base case
            if root.left is None and root.right is None:
                if total + root.val == sum:
                    path.append(root.val)
                    result.append(path)
            # split 
            else:
                if root.right is None:
                    dfs(root.left, path + [root.val], total + root.val)
                elif root.left is None:
                    dfs(root.right, path + [root.val], total + root.val)
                else:
                    dfs(root.left, path + [root.val], total + root.val)
                    dfs(root.right, path + [root.val], total + root.val)
        if root:
            dfs(root, [], 0)
        return result
                    