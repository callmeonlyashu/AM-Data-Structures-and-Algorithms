"""Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/"""

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])

        prev = points[0][1]
        balloons = 0
        
        for i in range(1, len(points)):
            # Check if the balloons can be burst with previous arrow
            # if yes burst the balloon
            if points[i][0] <= prev:
                balloons += 1
            # else set the prev pointer to current baloon
            else:
                prev = points[i][1]

        return len(points)-balloons



            
