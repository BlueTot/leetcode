class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0 for _ in prices]
        max_profits = [0 for _ in prices]
        for i in range(len(prices)):
            largest = 0
            for j in range(i):
                if prices[j] < prices[i]:
                    largest = max(largest, prices[i] - prices[j] + max_profits[j])
            profits[i] = largest
            if i > 0:
                max_profits[i] = max(max_profits[i-1], profits[i])
        return max_profits[-1]