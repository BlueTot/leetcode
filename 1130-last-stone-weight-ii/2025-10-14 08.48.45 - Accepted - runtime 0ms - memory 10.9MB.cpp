class Solution {
public:
    int lastStoneWeightII(vector<int>& stones) {
        
        int sum = 0;
        for (int weight : stones) {
            sum += 2*weight; // scale everything into positive zone
        }

        /* 0-1 knapsack dp array */
        vector<bool> dp(sum + 1, false);
        dp[0] = true;

        for (int i = 0; i < stones.size(); i++) {
            for (int j = sum; j >= stones[i]*2; j--) {
                dp[j] = dp[j] || dp[j-stones[i]*2];
            }
        }

        /* we want to find the smallest sum that is possible when
           we either subtract stones[i] or add stones[i] to the sum
           
           we ignore negative sums as that is not possible by the
           problem.
        */
        for (int j = sum / 2; j <= sum; j++) {
            if (dp[j])
                return j - sum / 2; // normalise
        }

        return 0;
    }
};