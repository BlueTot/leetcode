class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        
        vector<unordered_map<int, int>> dp(nums.size());
        int diff;
        int res = 0;

        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                diff = nums[i] - nums[j];
                dp[i][diff] = 1 + (dp[j].contains(diff) ? dp[j].at(diff) : 1);
            }
            for (auto pair : dp[i]) {
                res = max(res, pair.second);
            }
        }

        return res;
    }
};