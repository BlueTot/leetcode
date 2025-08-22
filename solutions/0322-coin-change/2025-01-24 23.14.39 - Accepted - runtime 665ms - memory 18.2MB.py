class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest = [None for _ in range(amount+1)]
        fewest[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                fewest[i] = 1
            else:
                poss = [fewest[i-val] for val in coins if i-val > 0 and fewest[i-val] is not None]
                if poss:
                    fewest[i] = 1 + min(poss)
        return fewest[amount] if fewest[amount] is not None else -1