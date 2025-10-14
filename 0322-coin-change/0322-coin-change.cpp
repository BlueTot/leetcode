class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

        /* complete knapsack approach */
        vector<int> dp(amount + 1, 1 << 30);
        dp[0] = 0;
        
        for (int i = 0; i < coins.size(); i++) {
            for (int j = coins[i]; j <= amount; j++) {
                dp[j] = min(dp[j], dp[j - coins[i]] + 1);
            }
        }

        return dp[amount] == 1 << 30 ? -1 : dp[amount];


    }
};