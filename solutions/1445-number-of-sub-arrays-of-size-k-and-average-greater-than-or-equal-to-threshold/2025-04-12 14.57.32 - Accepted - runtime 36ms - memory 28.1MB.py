class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        count = 0
        total = 0     
        
        for i in range(0, len(arr)):
            if i < k:
                total += arr[i]
            else:
                total += arr[i] - arr[i-k]
            if i >= k-1 and total >= k * threshold:
                count += 1
        
        return count
            