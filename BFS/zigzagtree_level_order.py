# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# intuitively BFS
class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            level = 0
            queue = [root]
            result = []
            while queue:
                if level%2 == 0:
                    result.append([node.val for node in queue])
                else:
                    result.append([node.val for node in queue][::-1])
                for i in range(len(queue)):
                    node = queue.pop(0)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                level += 1
            return result
        else:
            return []
        