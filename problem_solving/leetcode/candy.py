"""Link: https://leetcode.com/problems/candy/"""

# O(n) Solution
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n

        for i in range(n):
            #  check left
            if i-1 >= 0:
                if ratings[i-1] < ratings[i]:
                    candies[i] = candies[i-1] + 1

        for i in range(n-1, -1, -1):
            #  Check right
            if i+1 < n:
                if ratings[i+1] < ratings[i]:
                    candies[i] = max(candies[i], candies[i+1] + 1)


        return sum(candies)


# Solution with TLE O(n2)
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





