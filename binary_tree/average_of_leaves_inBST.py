# nothing special to say
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        result = []
        if root:
            level = [root]
            while level:
                level_total, level_count = 0, 0
                temp = []
                for node in level:
                    level_total += node.val
                    level_count += 1
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                level = temp
                result.append(level_total/level_count)
        return result