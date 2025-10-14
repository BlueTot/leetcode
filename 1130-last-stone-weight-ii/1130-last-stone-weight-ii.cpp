class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        
        int sum = 0;
        for (int weight : stones) {
            sum += 2*weight;
        }

        vector<bool> dp(sum + 1, false);
        dp[0] = true;

        for (int i = 0; i < stones.size(); i++) {
            for (int j = sum; j >= stones[i]*2; j--) {
                dp[j] = dp[j] || dp[j-stones[i]*2];
            }
        }

        for (int j = sum / 2; j <= sum; j++) {
            if (dp[j])
                return j - sum / 2;
        }

        return 0;
    }
};