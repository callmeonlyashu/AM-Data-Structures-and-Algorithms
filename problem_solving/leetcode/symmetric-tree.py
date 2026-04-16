""" Link: https://leetcode.com/problems/symmetric-tree/"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def find_invert(node):
            if not node:
                return node
            
            node.left, node.right = node.right, node.left
            find_invert(node.left)
            find_invert(node.right)
            return node

        def check_same_tree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            return check_same_tree(p.left, q.left) and check_same_tree(p.right, q.right)

        # print(invert_tree)
        return check_same_tree(root.left, find_invert(root.right))


