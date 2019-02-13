# this is rather a slow version
# pending for a better solution
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        
        # divide and conquer way
        def helper(preorder, inorder):
            # exit
            if not preorder:
                return None
            
            # split
            value = preorder[0]
            root = TreeNode(value)
            inorder_index = inorder.index(value)
            root.left = helper(preorder[1:1 + inorder_index], inorder[:inorder_index])
            root.right = helper(preorder[1+inorder_index:], inorder[1+inorder_index:])
            return root
        return helper(preorder, inorder)
        