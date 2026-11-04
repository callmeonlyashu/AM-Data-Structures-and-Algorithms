"""Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        n = len(candies)
        res = [False]*n

        curr_max = max(candies)
        for i in range(n):
            if candies[i] + extraCandies >= curr_max:
                res[i] = True
        
        return res
