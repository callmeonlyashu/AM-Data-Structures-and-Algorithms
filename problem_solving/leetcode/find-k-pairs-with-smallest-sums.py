"""Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/"""

# Solution with TLE
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        hp_pairs = []
        hp_sum = []
        heapq.heapify(hp_pairs)
        heapq.heapify(hp_sum)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                heapq.heappush(hp_pairs, (nums1[i], nums2[j]))
                heapq.heappush(hp_sum, nums1[i]+nums2[j])

        res = []
        for _ in range(k):
            curr_sum = heapq.heappop(hp_sum)
            for j, curr_pair in enumerate(hp_pairs):
                if sum(curr_pair) == curr_sum:
                    res.append(curr_pair)
                    del hp_pairs[j]
                    break
        
        return res
