"""Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/"""

# Much easier implementation
# Explanation: https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):     
            nonlocal max_sum       
            # base case
            if not node:
                return 0
            
            # recursing through left and right subtree
            left_max = dfs(node.left)
            right_max = dfs(node.right)

            # finding all the four paths and the maximum between all of them
            max_right_left = max(left_max, right_max)
            max_one_node_root = max(node.val, (node.val + max_right_left))
            max_all = max(max_one_node_root, left_max + right_max + node.val)

            # Storing the result in the maxSum holder
            max_sum = max(max_sum, max_all)

            # returning the value if root was part of the answer
            return max_one_node_root

        dfs(root)
        return max_sum


# Working approach:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def gain_from_subtree(node):
            nonlocal max_sum
            if not node:
                return 0

            # 1. Recursively get the max sum from left and right subtrees.
            # If the gain is negative, ignore it by taking max(..., 0).
            left_gain = max(gain_from_subtree(node.left), 0)
            right_gain = max(gain_from_subtree(node.right), 0)

            # 2. Price of the path if the current node is the highest point (the split point)
            current_path_sum = node.val + left_gain + right_gain

            # 3. Update the global maximum if this path is better
            max_sum = max(max_sum, current_path_sum)

            # 4. For the parent call, return the max path going down ONE branch
            return node.val + max(left_gain, right_gain)

        gain_from_subtree(root)
        return max_sum



# My Approach:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # Algo
        # 1. Create a new Tree with two values in Tree like a tuple
        # 2. First values should represent left sum and right one should 
        # represent right sum

        def create_dp_tree(root):
            if not root:
                return 

            root.val = (root.val, root.val)
            
            create_dp_tree(root.left)
            create_dp_tree(root.right)

        create_dp_tree(root)

        def dfs_child_sums(root):
            if not root:
                return
            
            dfs_child_sums(root.left)
            dfs_child_sums(root.right)

            left_sum = root.val[0]
            right_sum = root.val[1]
            if root.left:
                left_sum += root.left.val[0]
                right_sum += root.left.val[1]
            if root.right:
                left_sum += root.right.val[0]
                right_sum += root.right.val[1]

            root.val = (left_sum, right_sum)

        dfs_child_sums(root)

        max_sum=float("-inf")
        def dfs_find_max(root):
            nonlocal max_sum
            if not root:
                return
            
            max_sum = max(max_sum, root.val[0], root.val[0])
            dfs_find_max(root.left)
            dfs_find_max(root.right)
        
        dfs_find_max(root)
        return max_sum
        
