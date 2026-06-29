"""Link: https://leetcode.com/problems/candy/"""

# Solution with TLE
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n

        if n == 1:
            return sum(candies)

        for i in range(n):
            # First check left
            if i-1 >= 0:
                if ratings[i-1] < ratings[i]:
                    candies[i] = candies[i-1] + 1
            
            # Then go right until you find rating larger than current
            counter = 1
            j = i             
            while j+1 < n and ratings[j] > ratings[j+1]:
                counter += 1
                j += 1
            
            candies[i] = max(candies[i], counter)

        return sum(candies)





