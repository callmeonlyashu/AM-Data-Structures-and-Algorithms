"""Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/"""

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return f"Node({self.left} <- {self.val} -> {self.right})"

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque([root, None])

        # Get all the nodes in same level in list
        level_nodes = [[root, None]]
        cur_level = []
        while q:
            curr = q.popleft()

            if curr is None:
                level_nodes.append(cur_level)
                cur_level = []
            
                if len(q):
                    q.append(None)
                    continue

            if curr and curr.left:
                q.append(curr.left)
                cur_level.append(curr.left)

            if curr and curr.right:
                q.append(curr.right)
                cur_level.append(curr.right)
                
        # Loop through level nodes and assign them to next of current 
        for i in range(len(level_nodes)):
            for j in range(len(level_nodes[i])-1):
                if level_nodes[i][j]:
                    level_nodes[i][j].next = level_nodes[i][j+1]
        
        return root

            
        

                
