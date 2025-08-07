class Solution:
    def hIndex(self, citations: List[int]) -> int:
        print([len(citations) - i < citations[i] for i in range(len(citations))])





        left = -1
        right = len(citations)
        # if left == right:
        #     return min(citations[left], 1)
        while left < right:
            mid = (left + right) // 2
            print(left, right, mid)
            if len(citations) - mid < citations[mid]:
                right = mid
            else:
                left = mid + 1
        print(left, right)
        if left > 0:
            return max(len(citations)-left, citations[left-1])
        # if left > 0:
        #     return citations[left-1] if citations[left-1] > 0 else len(citations)-left
        return len(citations)
        # print(left-1)
        # return citations[left]
        # if left-1 == -1: # out of bounds
        #     return min(citations[0], 1)
        # return citations[left-1]