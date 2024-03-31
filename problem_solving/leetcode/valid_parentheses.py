"""
Link: https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.


Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brac = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for i in s:
            if i in brac.keys():
                stack.append(i)
            else:
               if not len(stack) or brac[stack.pop()] != i:
                   return False


        return len(stack) == 0



if __name__ == '__main__':
    sol = Solution()
    a = sol.isValid('()[]{}')
    b = sol.isValid('()')
    c = sol.isValid('(]')
    d = sol.isValid('"(){}}{"')
    e = sol.isValid('[')
    1==1