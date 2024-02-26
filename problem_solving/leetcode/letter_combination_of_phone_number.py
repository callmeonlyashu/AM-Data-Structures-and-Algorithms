"""
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

o any letters.


Example 1:

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

    Input: digits = ""
    Output: []
Example 3:

    Input: digits = "2"
    Output: ["a","b","c"]

"""


class Solution:
    def backtrack(self, index, path, digits, num_to_letter_dict, combinations):
        if index == len(digits):
            combinations.append(''.join(path))
            return

        for letter in num_to_letter_dict[digits[index]]:
            path.append(letter)
            self.backtrack(index + 1, path, digits, num_to_letter_dict, combinations)
            path.pop()

    def letterCombinations(self, digits: str) -> list[str]:
        num_to_letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        # Check if digits is empty
        if not digits:
            return []

        combinations = []

        self.backtrack(0, [], digits, num_to_letter_dict, combinations)
        return combinations


class Solution2:

    def letterCombinations(self, digits: str) -> list[str]:
        num_to_letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        # basic conditions
        if len(digits) == 1 and digits != ' ':
            return num_to_letter_dict[digits]

        if digits.isspace() or digits == '':
            return []

        # main logic here
        result_list = []
        result_dict = {}
        for d in digits:
            result_list.append(num_to_letter_dict[d])
            result_dict[d] = 0

        import itertools
        output = list(itertools.product(*result_list))

        res = [''.join(j) for j in output]
        return res

if __name__ == '__main__':
    sol = Solution()
    # b = sol.letterCombinations("23")
    # a = sol.letterCombinations("234")
