"""Link: https://leetcode.com/problems/word-pattern/"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        

        i = 0
        mapp = {}
        rev_map = {}
        while i < len(s_list):
            if pattern[i] not in mapp and s_list[i] not in rev_map:
                mapp[pattern[i]] = s_list[i]
                rev_map[s_list[i]] = pattern[i]
            else:
                if mapp.get(pattern[i]) != s_list[i]:
                    return False
                if rev_map.get(s_list[i]) != pattern[i]:
                    return False

            i += 1

        return True
