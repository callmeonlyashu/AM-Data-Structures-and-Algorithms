"""Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/"""

from typing import Optional, TreeNode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tree = TreeNode()
        res_node = tree
        def construct_tree(node): 
            if not node:
                return
            
            nonlocal res_node
            res_node.right = TreeNode(node.val)
            res_node = res_node.right 
            
            if node.left and res_node:
                construct_tree(node.left)

            if node.right and res_node:
                construct_tree(node.right)
        
        construct_tree(root)
        
        # copy tree back to root
        while tree.right:
            tree = tree.right
            if tree.right:
                root.right = TreeNode(tree.right.val)
            root.left = None
            root = root.right
