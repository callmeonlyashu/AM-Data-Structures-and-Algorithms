"""Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/"""

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        buy = [float('-inf')]*k
        sell = [0]*k

        
        for p in prices:
            for i in range(k):
                if i == 0:
                    buy[i] = max(buy[i],  -p)
                else:
                    buy[i] = max(buy[i],  sell[i-1]-p)
                sell[i] = max(sell[i], buy[i] + p)

        return sell[k-1]

