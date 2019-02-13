# optimal solution 
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # append the rightmost layer to result
        def helper(node, depth):
            if node:
                if depth == len(result):
                    result.append(node.val)
                helper(node.right, depth + 1)
                helper(node.left, depth + 1)
            
        result = []
        helper(root, 0)
        return result

# or BFS
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            level = [root]
            while level:
                result.append(level[-1].val)
                temp = []
                for node in level:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                level = temp
            
        return result       