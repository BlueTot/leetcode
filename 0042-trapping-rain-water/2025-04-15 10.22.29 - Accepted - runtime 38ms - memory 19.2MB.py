class Solution:
    def trap(self, height: List[int]) -> int:
        
        largestRight = []
        largest = 0
        for num in reversed(height):
            largest = max(largest, num)
            largestRight.append(largest)
        largestRight = largestRight[::-1]

        largestLeft = 0
        rainwater = 0
        for i, num in enumerate(height):
            minHeight = min(largestLeft, largestRight[i+1] if i < len(height)-1 else 0)
            rainwater += max(0, minHeight - num)
            largestLeft = max(largestLeft, num)
        return rainwater