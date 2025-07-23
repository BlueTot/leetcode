class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack = []
        result = [0 for _ in temperatures]
        for i in range(len(temperatures)):
            while mstack and temperatures[mstack[-1]] < temperatures[i]:
                j = mstack.pop()
                result[j] = i - j
            mstack.append(i)
        return result
                