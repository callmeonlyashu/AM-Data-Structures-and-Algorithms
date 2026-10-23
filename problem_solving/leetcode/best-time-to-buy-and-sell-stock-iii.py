"""Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1, sell1 = float('-inf'), 0
        buy2, sell2 = float('-inf'), 0
        for p in prices:
            buy1  = max(buy1,  -p)         # best after 1st buy
            sell1 = max(sell1, buy1 + p)   # best after 1st sell
            buy2  = max(buy2,  sell1 - p)  # best after 2nd buy (funded by 1st profit)
            sell2 = max(sell2, buy2 + p)   # best after 2nd sell
        return sell2
