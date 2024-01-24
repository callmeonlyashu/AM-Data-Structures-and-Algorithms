def match(text, pattern):
    if not pattern: return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    return first_match and match(text[1:], pattern[1:])

class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


if __name__ == '__main__':
    sol = Solution()
    # p = sol.isMatch("aaa", "a.a")
    # p1 = sol.isMatch("mississippi", "mis*is*ip*.")
    p2 = sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*b")
    1+1
    # s.isMatch("ab", ".*")
    # s.isMatch("aa", "a")
    # s.isMatch("mississippi", "mis*is*ip*.")