class Solution {
public:
    int integerBreak(int n) {

        // OPT[i] = maximum product by breaking i into parts
        vector<int> dp(n+1, 1);
        
        for (int i = 1; i <= n; i++) {

            // take off one number
            for (int j = 1; j < i; j++) {

                // either we take num * OPT[remaining] or remaining * num
                dp[i] = max({dp[i], (i - j) * dp[j], (i - j) * j});
            }

        }

        return dp[n];  
    }
};