class Solution:
    def hIndex(self, citations: List[int]) -> int:

        left = -1
        right = len(citations)

        # template to find minimum index that satisfies a condition
        while left < right:
            mid = (left + right) // 2

            # negate the condition to use template
            if len(citations) - mid < citations[mid]:
                right = mid
            else:
                left = mid + 1

        # at best we can have len(citations)-left as the H index
        if left > 0:
            return max(len(citations)-left, citations[left-1])
        return len(citations)
