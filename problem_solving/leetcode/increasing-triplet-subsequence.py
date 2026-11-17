"""Link: https://leetcode.com/problems/increasing-triplet-subsequence/"""

class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        subseq_dict = {}
        for n in nums:
            if n not in subseq_dict:
                subseq_dict[n] = [n]
            
            for k, v in subseq_dict.items():
                if k < n:
                    if v[-1] < n:
                        subseq_dict[k].append(n)
                    else:
                        v.pop()
                        subseq_dict[k].append(n)
                    
        for k, v in subseq_dict.items():
            if len(v) >= 3:
                return True
        
        return False
