"""Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]

        profits = 0
        for i in range(len(prices)):
            curr_min = min(prices[i], curr_min)
            
            pft = prices[i] - curr_min
            if pft > 0:
                profits += pft
                curr_min = prices[i]
        
        return profits


