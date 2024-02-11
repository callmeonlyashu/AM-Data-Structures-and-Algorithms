"""
Link: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        first_string = strs[0]
        result = ''
        for index in range(len(first_string)):
            total_match = []
            for other_str in strs[1:]:

                if index >= len(other_str):
                    total_match.append(False)
                elif first_string[index] == other_str[index]:
                    total_match.append(True)
                else:
                    total_match.append(False)

            if all(total_match):
                result += first_string[index]
            else:
                break

        return result


if __name__ == '__main__':
    sol = Solution()
    # sol.longestCommonPrefix(["flower","flow","flight"])
    # sol.longestCommonPrefix(["reflower", "flow", "flight"])
    # sol.longestCommonPrefix(["c","acc","ccc"])
    sol.longestCommonPrefix(["cir","car"])