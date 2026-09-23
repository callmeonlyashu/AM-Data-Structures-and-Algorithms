"""Link: https://leetcode.com/problems/ipo/"""

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()

        maxHeap = []
        i = 0
        for _ in range(k):
            # Keep pushing to maxHeap the profits if project is affordable
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1

            # if maxHeap is empty means no project is affordable
            if not maxHeap:
                break
            
            # -= is there as we are inserting in negative, -= will add them up
            w -= heapq.heappop(maxHeap)
        
        return w
