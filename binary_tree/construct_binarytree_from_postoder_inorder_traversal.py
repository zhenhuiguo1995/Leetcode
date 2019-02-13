# construct binary tree from postorder and inorder traversal
# divide and conquer solution
# pending for a better solution
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # divide and conuqer way
        def helper(inorder, postorder):
            # exit
            if not postorder:
                return None
            
            # split
            value = postorder[-1]
            root = TreeNode(value)
            index = inorder.index(value)
            root.left = helper(inorder[:index], postorder[:index])
            root.right = helper(inorder[index+1:], postorder[index:-1])
            return root
        return helper(inorder, postorder)