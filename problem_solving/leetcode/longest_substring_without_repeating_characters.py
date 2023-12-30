"""
URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if s.isspace() or len(s) == 1:
            return 1

        result_list = []
        substring = ''
        for i in range(len(s)):
            substring = s[i]
            for j in s[i + 1:]:
                if j not in substring:
                    substring += j
                    if len(s[i + 1]) == 1:
                        result_list.append(substring)
                else:
                    result_list.append(substring)
                    substring = ''
                    break

        result_dict = {sub: len(sub) for sub in result_list}
        output = max(result_dict.values())
        return output


if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring('rhytm')
    # s.lengthOfLongestSubstring('udsgtcazkdgyijogsuvspkqrfrmgyauufocatczdhidpttxlntgdfwwnnktnmqhrejtxmucveflxzkjmdrr')