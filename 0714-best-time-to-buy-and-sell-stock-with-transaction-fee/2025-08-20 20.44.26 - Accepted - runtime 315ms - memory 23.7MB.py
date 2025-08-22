class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        # at each point in time, you either hold stock or you don't
        hold = -float("inf")
        dont = 0 

        for i in range(len(prices)):
            prevhold, prevdont = hold, dont
            # either have yesterday's stock or have today's
            hold = max(prevhold, prevdont - prices[i])
            # either don't buy, or sell stock today
            dont = max(prevdont, prevhold + prices[i] - fee)
            print(hold, dont)

        return max(hold, dont)