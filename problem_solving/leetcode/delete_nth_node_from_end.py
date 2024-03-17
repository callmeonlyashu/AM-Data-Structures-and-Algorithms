"""
URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Worked fine on ChatGPT tests
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def count_nodes(self, nodes):
        cur_node = nodes
        count = 1
        while cur_node.next:
            count += 1
            cur_node = cur_node.next

        return count

    def removeNthFromEnd(self, head, n):
        total_nodes = self.count_nodes(head)

        if total_nodes == 0:
            return None
        elif total_nodes == 1 and n == 1:
            return None
        else:
            node_to_remove = total_nodes - n
            count = 0
            cur_node = head

            while cur_node.next:
                if count == node_to_remove - 1:
                    cur_node.next = cur_node.next.next
                    break

                cur_node = cur_node.next
            return head

    # Solution which worked
    def removeNthFromEnd_2(self, head, n):
        # Initialize two pointers: fast and slow
        slow = fast = head

        # Move the fast pointer ahead by n nodes
        for _ in range(n):
            fast = fast.next

        # Handle the case where the node to remove is the head node
        if not fast:
            return head.next

        # Move both pointers until the fast pointer reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return head



