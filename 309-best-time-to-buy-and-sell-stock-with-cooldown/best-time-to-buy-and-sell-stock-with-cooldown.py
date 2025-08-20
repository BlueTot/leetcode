class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        hold = [-float("inf"), -float("inf")]
        cash = [0, 0]

        for i in range(len(prices)):
            newhold = max(hold[1], cash[0] - prices[i])
            newcash = max(cash[1], hold[1] + prices[i])
            hold.pop(0)
            hold.append(newhold)
            cash.pop(0)
            cash.append(newcash)
        
            print(hold, cash)
        
        return max(hold[1], cash[1])