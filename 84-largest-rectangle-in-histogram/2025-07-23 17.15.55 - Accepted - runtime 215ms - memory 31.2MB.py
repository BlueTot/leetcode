class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        next_smallest = [n for _ in heights]
        mstack = []
        for i in range(n):
            while mstack and heights[mstack[-1]] > heights[i]:
                j = mstack.pop()
                next_smallest[j] = i
            mstack.append(i)

        prev_smallest = [-1 for _ in heights]
        mstack = []
        for i in range(n-1, -1, -1):
            while mstack and heights[mstack[-1]] > heights[i]:
                j = mstack.pop()
                prev_smallest[j] = i
            mstack.append(i)

        largest = 0
        for i in range(n):
            j, k = next_smallest[i], prev_smallest[i]
            area = heights[i] * (j - k - 1)
            largest = max(largest, area)
        
        return largest