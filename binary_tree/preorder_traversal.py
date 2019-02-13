# preorder traversal of a binary tree

# recursive version
def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    result = []
    
    # definition
    def helper(root):
        # exit
        if not root:
            return
        
        # split
        result.append(root.val)
        helper(root.left)
        helper(root.right)
    
    helper(root)
    return result


# iterative version: intuitively use a stack
# use a rights stack to record the right nodes
def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return []
    else:
        result, rights = [], []
        curr = root
        while curr:
            result.append(curr.val)
            if curr.right:
                rights.append(curr.right)
            curr = curr.left
            if curr is None and rights:
                curr = rights.pop()
        return result
    