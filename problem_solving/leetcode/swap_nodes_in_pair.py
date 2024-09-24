"""
Link: https://leetcode.com/problems/swap-nodes-in-pairs/

Description:

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]

Example 4:
    Input: head = [1,2,3]
    Output: [2,1,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        first_node = head
        second_node = head.next
        update_node = self.swapPairs(second_node.next)
        first_node.next = update_node
        second_node.next = first_node
        return second_node



if __name__ == '__main__':
    sol = Solution()
    list2 = ListNode(1)
    list2.next = ListNode(2)
    list2.next.next = ListNode(3)
    list2.next.next.next = ListNode(4)

    res = sol.swapPairs(list2)
    1==1
