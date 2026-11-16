"""Link: https://leetcode.com/problems/unique-number-of-occurrences/"""

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occ_dict = defaultdict(int)

        for n in arr:
            occ_dict[n] += 1

        return len(occ_dict.values()) == len(set(occ_dict.values()))
      
