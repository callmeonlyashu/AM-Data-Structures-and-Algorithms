"""Link: https://leetcode.com/problems/binary-tree-right-side-view/"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root, None])
        res = []
        level = []
        while queue:
            cur_element = queue.pop()

            if cur_element:
                level.append(cur_element.val)

            if cur_element is None:
                if level:
                    res.append(level[0])

                level = []
                if len(queue):
                    queue.appendleft(None)
                    continue

            if cur_element and cur_element.right:
                queue.appendleft(cur_element.right) 
                
            if cur_element and cur_element.left:
                queue.appendleft(cur_element.left)

        return res
