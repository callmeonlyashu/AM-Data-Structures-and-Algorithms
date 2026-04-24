"""Link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/"""

# Approach 1:

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        all_nodes = []
        def dfs(node, diff=[]):
            if not node:
                return diff

            diff.append(node.val)
            left_min = dfs(node.left, diff)
            right_min = dfs(node.right, diff)

        dfs(root, all_nodes)
        # print(f"diff: {all_nodes}")

        min_diff = float("+inf")
        for i in range(len(all_nodes)):
            for j in range(i+1, len(all_nodes)):
                min_diff = min(min_diff, abs(all_nodes[i] - all_nodes[j]))
            
        return min_diff
