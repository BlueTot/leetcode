class Solution {
public:
    int numDistinct(string s, string t) {
        
        vector<vector<unsigned long long>> dp(
            s.length() + 1, vector<unsigned long long>(t.length() + 1, 0)
        );

        for (int i = 0; i <= s.length(); i++) {
            for (int j = 0; j <= t.length(); j++) {
                
                /* j is the empty string */
                if (j == 0) {
                    dp[i][j] = 1; // one way only, as there is only one empty subset

                } else if (i > 0) {
                    
                    /* if we don't use the current character */
                    dp[i][j] = dp[i-1][j];

                    /* we can only use the current character if they are the same */
                    if (s[i-1] == t[j-1])
                        dp[i][j] += dp[i-1][j-1]; // remove current character
                }
            }
        }

        return dp[s.length()][t.length()];
    }
};
