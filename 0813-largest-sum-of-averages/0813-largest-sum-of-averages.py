class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        
        n = len(nums)
        dp = [[0 for _ in range(k)] for _ in range(n)]
        
        # prefix sum - prefix[r+1] - prefix[l] = sum(l..r)
        prefix = [0 for _ in range(n+1)]
        curr = 0
        for i in range(n):
            curr += nums[i]
            prefix[i+1] = curr
        
        # 2d dp
        for i in range(n):
            for j in range(k):

                if j > 0:
                    res = 0
                    for p in range(0, i): # up to but not including i
                        # average from p+1 to i
                        curr_avg = (prefix[i+1] - prefix[p+1]) / (i - p)
                        res = max(res, dp[p][j-1] + curr_avg)
                    dp[i][j] = max(dp[i][j-1], res)
                
                else:
                    dp[i][j] = (prefix[i+1] - prefix[0]) / (i + 1)
        
        return dp[n-1][k-1]
                