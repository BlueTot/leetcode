class Solution {
public:
    int numSquares(int n) {

        /* calculate the squares */
        vector<int> squares;
        int sqrt = 0;
        while (sqrt * sqrt <= n) {
            squares.push_back(sqrt * sqrt);
            sqrt++;
        }

        /* complete knapsack */
        vector<int> dp(n + 1, 1 << 30);
        dp[0] = 0;

        for (int i = 0; i < squares.size(); i++) {
            for (int j = squares[i]; j <= n; j++) {
                dp[j] = min(dp[j], dp[j - squares[i]] + 1);
            }
        }

        return dp[n];
    }
};