class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1

        def isCloser(a, b, x):
            return abs(a-x) < abs(b-x) or (abs(a-x) == abs(b-x) and a < b)
        
        while right - left + 1 > k:
            if isCloser(arr[left], arr[right], x):
                right -= 1
            else:
                left += 1

        return arr[left:right+1]