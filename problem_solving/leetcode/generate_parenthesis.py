"""
Link: https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:
    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
    Input: n = 1
    Output: ["()"]

"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(curr, open_count, close_count):
            if len(curr) == 2 * n:
                result.append(curr)
                return
            if open_count < n:
                backtrack(curr + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr + ')', open_count, close_count + 1)

        result = []
        backtrack('', 0, 0)
        return result


if __name__ == '__main__':
    sol = Solution()
    a = sol.generateParenthesis(3)
    1==1