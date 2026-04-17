"""Link: https://leetcode.com/problems/path-sum/"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, curr_sum=0, found=False, curr_arr=[]):            

            if node and node.left is None and node.right is None:
                curr_sum += node.val

                if curr_sum == targetSum:
                    found = True
                return found

            if node:
                curr_sum += node.val
                
                found = dfs(node.left, curr_sum, found)
                found = dfs(node.right, curr_sum, found)
            return found

        return dfs(root)

        
