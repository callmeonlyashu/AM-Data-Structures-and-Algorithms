"""Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        queue = deque([root, None])

        level_arr = []

        res = []
        while queue:
            curr_element = queue.popleft()
            if curr_element:
                level_arr.append(curr_element.val)

            if curr_element is None:
                curr_avg = sum(level_arr)/len(level_arr)
                res.append(curr_avg)

                level_arr = []
                if len(queue):
                    queue.append(None)
                    continue

            if curr_element and curr_element.left:
                queue.append(curr_element.left)
            
            if curr_element and curr_element.right:
                queue.append(curr_element.right)
            
        return res


