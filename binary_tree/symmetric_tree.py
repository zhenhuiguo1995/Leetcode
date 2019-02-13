# recursive solution
# Special problem: discuss the tree with left and right
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # given two nodes left and right
        # return a boolean represneting if the two sub tree are symmetric
        def helper(left, right):
            # exit
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            else:
                return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
            
        if root:
            return helper(root.left, root.right)
        return True


# iterative solution
# deals with left and right, respectively
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # iterative solution using queue 
        if root:
            left = [root.left]
            right = [root.right]
            while left and right:
                left_node, right_node = left.pop(0), right.pop(0)
                if left_node is None and right_node is None:
                    continue
                elif left_node is None or right_node is None:
                    return False
                elif left_node.val != right_node.val:
                    return False
                else:
                    left.append(left_node.left)
                    left.append(left_node.right)
                    right.append(right_node.right)
                    right.append(right_node.left)
            
        return True
            
  