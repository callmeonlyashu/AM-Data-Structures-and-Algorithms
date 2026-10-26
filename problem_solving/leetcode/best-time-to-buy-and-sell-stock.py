"""Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/"""

class Solution:    
    def maxProfit(self, prices: List[int]) -> int:
        dp = []
        min_price_so_far = float('inf')

        for i in range(len(prices)):
            if prices[i] < min_price_so_far:
                min_price_so_far = prices[i]

            curr_profit = prices[i] - min_price_so_far
            dp.append(curr_profit)

        return max(dp)
      
