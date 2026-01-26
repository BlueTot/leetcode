class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        res = []
        arr.sort()

        minimum = float("inf")
        for i in range(0, len(arr)-1):
            minimum = min(minimum, arr[i+1] - arr[i])
        
        for i in range(0, len(arr)-1):
            if arr[i+1]-arr[i] == minimum:
                res.append([arr[i], arr[i+1]])
        
        return res