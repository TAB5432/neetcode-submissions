# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(root1, root2):
            if not root1 and not root2:
                return True
            
            if root1 and root2 and root1.val == root2.val:
                return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)
            return False

        def check_subtree(root, subRoot):
            if not subRoot:
                return True
            
            if not root:
                return False
                
            if is_identical(root, subRoot):
                return True
            
            return check_subtree(root.left, subRoot) or check_subtree(root.right, subRoot)
        
        return check_subtree(root, subRoot)