"""Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/"""

# Solution with TLE

from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        tree = TreeNode()
        total_nodes = len(postorder)
        tree.val = postorder[-1]

        for i in range(total_nodes-2, -1, -1):
            node = tree
            while node:
                curr_val = postorder[i]
                # Check in in-order if it should be on the right or left of node
                curr_root = node.val
                idx_curr_root = inorder.index(curr_root)
                idx_curr_val = inorder.index(curr_val)

                # If current index is greater, then go right else left
                if idx_curr_val > idx_curr_root:
                    if node.right is None:
                        node.right = TreeNode(curr_val)
                        break
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        node.left = TreeNode(curr_val)
                        break
                    else:
                        node = node.left

        return tree


        
