class Solution {
public:
    bool canPartition(vector<int>& nums) {

        /* we want each subset to have half the sum */
        long long sum = 0;
        for (int num : nums)
            sum += (long long) num;
        
        if (sum % 2 == 1) return false;
        sum /= 2;
        
        /* dp[i][j] is the number of ways to get sum j using
        the first i elements */
        vector<vector<bool>> dp(nums.size(), vector<bool>(sum + 1,false));
        dp[0][0] = true;

        for (int i = 0; i < nums.size(); i++) {
            for (long long j = 0; j <= sum; j++) {
                if (i == 0) {
                    if (j == 0)
                        dp[i][j] = true;
                    else
                        dp[i][j] = nums[i] == (long long) j;
                } else {
                    dp[i][j] = dp[i-1][j];
                    if (j >= (long long) nums[i])
                        dp[i][j] = dp[i][j] || dp[i-1][j - nums[i]];
                }
            }
        }
        
        return dp[nums.size()-1][sum] > 0;
    }
};