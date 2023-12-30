"""
Link: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        number1 = self.convertLinkedListToNumber(l1)
        number2 = self.convertLinkedListToNumber(l2)
        total = number2 + number1
        return self.convertNumberToLinkedList(total)

    def convertLinkedListToNumber(self, list_node):
        number2 = 0
        i = 0
        while list_node.next is not None:
            number2 = number2 + (list_node.val * (10 ** i))
            list_node = list_node.next
            i += 1
        number2 = number2 + (list_node.val * (10 ** i))
        return number2

    def convertNumberToLinkedList(self, number):
        myarray = []
        while number // 10 > 0:
            myarray.append(number % 10)
            number = number // 10
        myarray.append(number)

        list_node = ListNode(myarray[0])
        current_node = list_node
        for i in myarray[1:]:
            current_node.next = ListNode(i)
            current_node = current_node.next

        return list_node


if __name__ == '__main__':
    pass