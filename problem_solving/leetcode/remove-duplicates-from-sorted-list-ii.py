"""Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        res = ListNode()
        res_head = res
        duplicates = set()
        while curr:
            if curr.next and curr.val == curr.next.val:
                duplicates.add(curr.val)
            else:
                if curr.val not in duplicates:
                    res_head.next = ListNode(curr.val)
                    res_head = res_head.next
            curr = curr.next

        if curr:
            res.next(curr)

        return res.next
    
