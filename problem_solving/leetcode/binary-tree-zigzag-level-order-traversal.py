"""Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root, None])

        res = []
        curr_level = []
        level = 1
        while queue:
            curr_node = queue.popleft()
            if curr_node:
                curr_level.append(curr_node.val)

            if curr_node is None:
                if level % 2 == 0:
                    curr_level = curr_level[::-1]

                res.append(curr_level)
                curr_level = []
                level += 1

                if len(queue):
                    queue.append(None)
            
            if curr_node and curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node and curr_node.right:
                queue.append(curr_node.right)

        return res
