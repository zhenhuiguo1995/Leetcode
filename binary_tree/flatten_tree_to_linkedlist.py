"""
Divide and conquer
Suppose the left sub-tree and right sub-tree are already flattened, 
1. set the right sub-tree as the right sub-tree of the last node in the left sub-tree
2. sets root.right to the root of left sub-tree, 
3. sets root.left to None 

Hence the return value will consists of two: the root and the leaf
base case:
    1. when the node given is None
    2. when the node given is a leaf node
split (divide and conquer part):
    1. get the left/right root/leaf
    2. consider necessary conditins
    3. don't forget return value

Remember: under an situation, the helper method will have a return value in
the format as a tuple(or a list of two values)
"""
class Solution(object):
    def flatten(self, root):
        
        # definition
        def helper(root):
            # exit a.k.a. base case
            if root is None:
                return None, None
            elif root.left is None and root.right is None:
                return root, root
            
            # split
            # divide 
            left_root, left_leaf = helper(root.left)
            right_root, right_leaf = helper(root.right)
            # conquer
            if left_leaf is not None:
                left_leaf.right = right_root
                root.right = left_root
                root.left = None
            if right_leaf is None:
                right_leaf = left_leaf
            return root, right_leaf
        
        helper(root)