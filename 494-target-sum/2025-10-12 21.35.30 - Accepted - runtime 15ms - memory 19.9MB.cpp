class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        
        /* we can turn this directly into a 0-1 knapsack
        by adding every number to target, so adding will be "taking a number"
        and subtracting will be "doing nothing" */ 

        int W = target;
        for (int num : nums)
           W += num;

        if (W < 0) return 0;

        /* dp[i][j] is the number of ways to get target j using the first i numbers */
        vector<vector<int>> dp(nums.size(), vector<int>(W + 1, 0));

        for (int i = 0; i < nums.size(); i++) {
            for (int t = 0; t <= W; t++) { 
                if (i == 0) {
                    if (t == 0)
                        dp[i][t] = 1 + (nums[i] == 0);
                    else
                        dp[i][t] = nums[i] * 2 == t;
                } else {
                    dp[i][t] = dp[i-1][t];
                    if (t >= nums[i] * 2)
                        dp[i][t] += dp[i-1][t - nums[i] * 2];
                }
            }
        }

        return dp[nums.size()-1][W];  
    }
};