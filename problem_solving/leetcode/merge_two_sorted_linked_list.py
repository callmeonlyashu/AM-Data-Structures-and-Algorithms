"""
Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

Description:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        result_list = []

        cur_node1 = list1

        if cur_node1:
            while cur_node1.next:
                result_list.append(cur_node1.val)
                cur_node1 = cur_node1.next

            result_list.append(cur_node1.val)

        cur_node2 = list2

        if cur_node2:
            while cur_node2.next:
                result_list.append(cur_node2.val)
                cur_node2 = cur_node2.next

            result_list.append(cur_node2.val)

        if not len(result_list):
            return None

        result_list.sort()

        output = ListNode(result_list[0])
        curr_node = output
        for element in result_list[1:]:
            curr_node.next = ListNode(element)
            curr_node = curr_node.next

        return output



if __name__ == '__main__':
    sol = Solution()
    # list1 = ListNode(1)
    # list1.next = ListNode(2)
    # list1.next.next = ListNode(4)
    #
    # list2 = ListNode(1)
    # list2.next = ListNode(3)
    # list2.next.next = ListNode(4)

    list1 = ListNode(4)
    list1.next = ListNode(7)
    list1.next.next = ListNode(9)

    list2 = ListNode(6)
    list2.next = ListNode(9)
    list2.next.next = ListNode(11)
    list2.next.next.next = ListNode(15)

    a = sol.mergeTwoLists(list1, list2)
    1==1