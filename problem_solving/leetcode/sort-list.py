"""Link: https://leetcode.com/problems/sort-list/"""

# Bubble Sort Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        sorted_list = False
        while not sorted_list:
            sorted_list = True
            curr = head
            
            while curr and curr.next:
                
                if curr.val > curr.next.val:
                    curr.val, curr.next.val = curr.next.val, curr.val
                    sorted_list = False
                curr = curr.next
            
        return head
