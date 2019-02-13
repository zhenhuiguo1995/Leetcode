# inorder traversal for binary tree

# recursive solution (with traversal)
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # global variable 
    result = []
    
    #definition
    def helper(root):
        # exit
        if root is None:
            return
        # split
        helper(root.left)
        result.append(root.val)
        helper(root.right)
    
    helper(root)
    return result


#iterative solution
# it is intuitive to use a stack for an iterative solution
# it it is just preorder, it would be much more easier 
# for inorder, there is a little "backtracking" with the stack.
# First we put as much as possible left nodes of the root node
# pops out a node and add it, checks for its right nodes
# (every node in the stack, their left nodes are in the stack, their right
# node may not be in the stack)
 
def inorderTraversal(root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        else:
            stack = []
            curr = root
            result = []
            while curr or stack:
                while curr is not None:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                result.append(curr.val)
                curr = curr.right
            return result


    