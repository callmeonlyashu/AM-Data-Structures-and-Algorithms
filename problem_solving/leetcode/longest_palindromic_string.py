"""
URL: https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ''
        if len(s) == 1:
            return s

        for i in range(len(s)):
            sub = s[i]
            if self.is_palindrome(s[i]) and len(max_str) < len(s[i]):
                max_str = s[i]
            for j in range(i + 1, len(s)):
                sub = sub + s[j]
                if self.is_palindrome(sub) and len(max_str) < len(sub):
                    max_str = sub
        return max_str

    def is_palindrome(self, string):
        return string == string[::-1]

