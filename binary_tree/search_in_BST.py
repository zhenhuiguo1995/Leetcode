# recursive solution
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # returns the tree with root.val = val
        def binary_search(root):
            # exit
            if root is None:
                return []
            else:
                if root.val == val:
                    return root
                elif root.val < val:
                    return binary_search(root.right)
                else:
                    return binary_search(root.left)
        return binary_search(root)

# iterative solution
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root:
            while root is not None:
                if root.val == val:
                    return root
                elif root.val < val:
                    root = root.right
                else:
                    root = root.left    
        return []
        