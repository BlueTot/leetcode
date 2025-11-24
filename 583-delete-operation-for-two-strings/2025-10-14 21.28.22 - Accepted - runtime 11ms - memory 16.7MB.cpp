class Solution {
public:
    int minDistance(string word1, string word2) {
        
        vector<vector<int>> dp(word1.length() + 1, vector<int>(word2.length() + 1, 1 << 30));

        /* base cases */
        dp[0][0] = 0;
        for (int i = 1; i <= word1.length(); i++)
            dp[i][0] = i;
        for (int j = 1; j <= word2.length(); j++)
            dp[0][j] = j;

        /* 2d dp */
        for (int i = 0; i < word1.length(); i++) {
            for (int j = 0; j < word2.length(); j++) {
                if (word1[i] == word2[j]) {
                    dp[i+1][j+1] = dp[i][j];
                } else {
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + 1;
                }
            }
        }

        return dp[word1.length()][word2.length()];
    }
};