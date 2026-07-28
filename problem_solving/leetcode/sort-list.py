"""Link: https://leetcode.com/problems/sort-list/"""

# Merge Sort Approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1: cur.next = l1
            if l2: cur.next = l2
            return dummy.next

        if not head or not head.next:
            return head
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        left = self.sortList(head)
        right = self.sortList(slow)
        return merge(left, right)


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
