"""Link: https://leetcode.com/problems/binary-search-tree-iterator/"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = []
        self.index = 0
        def inorder(root):
            if not root:
                return root
            
            inorder(root.left)
            self.inorder.append(root.val)
            inorder(root.right)

        inorder(root)
            
    def next(self) -> int:
        # print("elements", self.inorder)
        curr_element = self.inorder[self.index]
        self.index += 1
        return curr_element 

    def hasNext(self) -> bool:
        if self.index + 1 <= len(self.inorder):
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
