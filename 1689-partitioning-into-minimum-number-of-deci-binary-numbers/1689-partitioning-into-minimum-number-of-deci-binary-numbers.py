class Solution:
    def minPartitions(self, n: str) -> int:

        # 0
        # 1
        # 10
        # 11
        # 100
        # 101
        # 110
        # 111
        # 1000

        largest = 0
        for char in n:
            largest = max(largest, int(char))
        
        return largest

        