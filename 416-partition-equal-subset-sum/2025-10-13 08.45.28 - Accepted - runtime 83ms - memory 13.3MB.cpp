class Solution {
public:
    bool canPartition(vector<int>& nums) {

        /* we want each subset to have half the sum */
        long long sum = 0;
        for (int num : nums)
            sum += (long long) num;
        
        if (sum % 2 == 1) return false;
        sum /= 2;
        
        /* dp[j] is the number of ways to get sum j on each iteration.
           we continually replace the dp array to do 2d dp
           using 1d space */

        vector<bool> dp(sum + 1, false);
        dp[0] = true;

        for (int i = 0; i < nums.size(); i++) {
            for (long long j = sum; j >= nums[i]; j--) {
                dp[j] = dp[j] || dp[j - nums[i]];
            }
        }

        return dp[sum];
    }
};