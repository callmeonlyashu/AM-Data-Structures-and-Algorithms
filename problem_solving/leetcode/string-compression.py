"""Link: https://leetcode.com/problems/string-compression/"""

class Solution:
    def compress(self, chars: list[str]) -> int:
        groups = []

        char_count = 1
        i = 0
        for i in range(1, len(chars)):
            if chars[i-1] == chars[i]:
                char_count += 1
            else:
                groups.append(chars[i-1])
                if char_count != 1:
                    groups.append(str(char_count))
                char_count = 1
        
        groups.append(chars[i])
        if char_count != 1:
            groups.append(str(char_count))

        res = []
        for gp in groups:
            res.extend(list(gp))
        
        chars[:] = res
        return len(chars)

        
