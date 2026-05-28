"""Link: https://leetcode.com/problems/rotate-list/"""

from typing import Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_length_of_list(node):
            if not node:
                return 0
            
            return 1 + get_length_of_list(node.next)
        
        # Get the starting index of rotation
        total_elements = get_length_of_list(head)
        rotate_index = 0
        if total_elements:
            rotate_index = abs((k%total_elements) - total_elements)
    
        # If no elements or one element in head
        if total_elements <= 1 or not rotate_index:
            return head
        
        # If k == 0, no rotation needed
        if not k:
            return head

        node = head
        count = 1
        rot_node = None
        # Remove the elements from the index of rotation
        while node:
            if count == rotate_index:
                rot_node = node.next
                node.next = None
                break

            node = node.next
            count += 1
        
        # Append the head to the end of rot_head
        rev_node = rot_node
        while rev_node and rev_node.next:
            rev_node = rev_node.next

        if rev_node:
            rev_node.next = head
        else:
            rot_node = head

        return rot_node
        



            
