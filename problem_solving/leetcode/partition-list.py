"""Link: https://leetcode.com/problems/partition-list/"""

# Non-Two pointer solution

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        main_node = head
        
        copy_head = ListNode()
        copy_node = copy_head

        res = ListNode()
        res_node = res
        while main_node:
            if main_node.val >= x:
                copy_node.next = ListNode(main_node.val)
                copy_node = copy_node.next
            else:
                res_node.next = ListNode(main_node.val)
                res_node = res_node.next

            main_node = main_node.next


        res_node.next = copy_head.next
        return res.next
        
