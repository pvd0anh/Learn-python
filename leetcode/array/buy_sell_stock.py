class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if (n <= 1):
            return 0

        i = 0
        profit = 0
        while prices[i + 1] <= prices[i]:
            i += 1
            if (i == n - 1):
                return 0
        
        while (i < (n - 1)):
            buy = i
            i += 1
            while ((i < n) and (prices[i] >= prices[i - 1])):
                i += 1
            sell = i - 1
            profit += prices[sell] - prices[buy]
        return profit
