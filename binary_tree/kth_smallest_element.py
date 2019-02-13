# recursive way
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # returns the number of nodes in the tree rooted at root
        def get_nodes_num(root):
            # exit
            if root is None:
                return 0
            return 1 + get_nodes_num(root.left) + get_nodes_num(root.right)
        
        def helper(root, k):
            temp = get_nodes_num(root.left)
            if temp + 1 == k:
                return root.val
            elif temp + 1 < k:
                return helper(root.right, k - (temp + 1))
            else:
                return helper(root.left, k)
                
        return helper(root, k)