# inorder traversal of a binary search tree will be in 
# increasing order
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        result = []
        def inorder(root):
            # exit
            if root is None:
                return
            else:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        inorder(root)
        for i in range(0, len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
        return True