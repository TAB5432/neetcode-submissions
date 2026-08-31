# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []

        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node)
            node = node.right




        res = []

        def in_order(node):
            if not node: return 

            in_order(node.left)
            res.append(node.val)
            in_order(node.right)

        in_order(root)
        return res