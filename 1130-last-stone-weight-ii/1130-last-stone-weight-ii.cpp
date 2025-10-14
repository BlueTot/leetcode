class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        
        int sum = 0;
        for (int weight : stones) {
            sum += 2*weight;
        }

        vector<vector<bool>> dp(stones.size(), vector<bool>(sum + 1, false));
        for (int i = 0; i < stones.size(); i++) {
            for (int j = 0; j <= sum; j++) {
                if (i == 0) {
                    if (j == 0)
                        dp[i][j] = true;
                    else
                        dp[i][j] = stones[i]*2 == j;
                } else {
                    dp[i][j] = dp[i-1][j];
                    if (j >= stones[i]*2)
                        dp[i][j] = dp[i][j] || dp[i-1][j-stones[i]*2];
                }
            }
        }

        for (int j = sum / 2; j <= sum; j++) {
            if (dp[stones.size()-1][j])
                return j - sum / 2;
        }

        return 0;
    }
};