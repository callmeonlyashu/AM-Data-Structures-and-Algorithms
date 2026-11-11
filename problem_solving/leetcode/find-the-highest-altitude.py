"""Link: https://leetcode.com/problems/find-the-highest-altitude/"""

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr_gain = 0

        alt = 0
        for i in range(len(gain)):
            curr_gain += gain[i]
            alt = max(alt, curr_gain)

        return alt
      
