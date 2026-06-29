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
            # For first element, check right only
            if i == 0:
                if ratings[i] > ratings[i+1]:
                    candies[i] = candies[i+1] + 1

            # For last element, check left only
            elif i == n-1:
                if ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1] + 1

            # For element in middle, first check max of left and right
            else:
                if ratings[i] > ratings[i-1]:
                    candies[i] = candies[i-1] + 1
                
                if ratings[i] > ratings[i+1]:
                    if candies[i] < candies[i+1] + 1:
                        candies[i] = candies[i+1] + 1

                # Sync all the previous elements to increase the candies if neighbours updated.
                j = i
                while j > 0:
                    if ratings[j] < ratings[j-1]:
                        candies[j-1] = max(candies[j-1], candies[j] + 1)
                    j -= 1
        
        return sum(candies)



