"""Link: https://leetcode.com/problems/ransom-note/"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        cnt1 = dict(Counter(ransomNote))
        cnt2 = dict(Counter(magazine))

        for key, val in cnt1.items():
            if val > cnt2.get(key, 0):
                return False
        
        return True
