# postorder traversal of a binary tree

# recursive version
def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # global variable
    result = []
    
    # definition
    def helper(root):
        # exit
        if not root:
            return
        
        # split
        else:
            helper(root.left)
            helper(root.right)
            result.append(root.val)
    
    helper(root)
    return result
    
#iterative version
def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # iterative version
    stack = []
    result = []
    p = root
    while p or stack:
        if p is not None:
            stack.append(p)
            result.insert(0, p.val)
            p = p.right
        else:
            p = stack.pop()
            p = p.left
    return result