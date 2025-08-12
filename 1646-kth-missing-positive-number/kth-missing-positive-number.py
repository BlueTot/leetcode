class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        def search(nums):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                num_missing = arr[mid] - (mid + 1)
                if num_missing >= k:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        pos = search(arr) - 1
        value = 0 if pos == -1 else arr[pos]
        missing_so_far = value - (pos + 1)
        print(pos)
        print(missing_so_far)
        return value + (k - missing_so_far)