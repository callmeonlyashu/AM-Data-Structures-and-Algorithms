"""

URL: https://leetcode.com/problems/regular-expression-matching/description/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".
    Example 2:

    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
    Example 3:

    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

"""

class Solution():

    def recussiveConverter(self, pattern, string, length, my_result=[], counter=-1):
        for k in range(len(pattern)):

            if pattern[k] == '*':
                for l in range(length):
                    possible_string = pattern[:k-1] + pattern[k-1]*l + pattern[k+1:]
                    # result.append(possible_string)
                    my_result.append(possible_string)
                break

        counter += 1

        if string in my_result:
            return my_result

        if len(my_result) and '*' in my_result[counter]:
            return self.recussiveConverter(my_result[counter], string,  length, my_result, counter)
        else:
            return my_result


    def isMatch(self, s: str, p: str) -> bool:

        if s==p:
            return True

        # Check general chars matching first

        star_count = 0
        for ch in range(len(p)):
            if p[ch] == '*':
                star_count += 1

        if star_count > 0:
            total_length = abs(len(s))+1
            strings = self.recussiveConverter(p, s, total_length, [])
        else:
            strings = [p]

        # if it matches any string without '.'
        if s in strings:
            return True
        # if it doesn't matche any string check
        # for '.' pattern string with length eq to s
        else:
            filtered = [f for f in strings if len(s) == len(f)]

            final_match = []
            for f_s in filtered:
                match = []
                for ind in range(len(f_s)):
                    if f_s[ind] == s[ind]:
                        match.append(True)
                    elif f_s[ind] == '.':
                        match.append(True)
                    else:
                        match.append(False)

                final_match.append(match)

            if len(final_match):
                for f in final_match:
                    if all(f):
                        return True
                return False

            else:
                return False

if __name__ == '__main__':
    sol = Solution()
    # p = sol.isMatch("aaa", "a.a")
    # p1 = sol.isMatch("mississippi", "mis*is*ip*.")
    p2 = sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*b")
    1+1
    # s.isMatch("ab", ".*")
    # s.isMatch("aa", "a")
    # s.isMatch("mississippi", "mis*is*ip*.")
