""" Link: https://leetcode.com/problems/reverse-linked-list-ii/"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        llist = ListNode()
        new_list = llist

        # Get the linked list from the range left and right.
        curr = head
        i = 1
        while i <= right:
            if i >= left:
                new_list.next = ListNode(curr.val)
                new_list = new_list.next
            curr = curr.next
            i += 1

        # Reverse the LinkedList
        myhead = llist.next
        revhead = None
        while myhead:
            nd = ListNode(myhead.val)
            nd.next, revhead = revhead, nd
            myhead = myhead.next

        # Now append the reversed list into main List
        res = ListNode()
        rhead = res
        curr = head

        for i in range(1, right+1):

            if i == left:
                rhead.next = revhead
            elif i > left and i <= right:
                curr = curr.next
                rhead = rhead.next
                continue
            else:
                rhead.next = ListNode(curr.val)
            
            curr = curr.next
            rhead = rhead.next

        if curr:
            rhead.next = curr

        return res.next
