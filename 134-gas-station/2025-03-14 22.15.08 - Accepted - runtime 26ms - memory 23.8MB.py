class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(diffs := [g - c for g, c in zip(gas, cost)]) < 0:
            return -1
        total = 0
        index = 0
        for i in range(len(gas)):
            total += diffs[i]
            if total < 0:
                total = 0
                index = i + 1
        return index