class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        
        vector<pair<int, int>> nums;
        for (int i = 0; i < strs.size(); i++) {
            int zeroes = 0, ones = 0;
            for (char s : strs[i]) {
                if (s == '0') {
                    zeroes++;
                } else {
                    ones++;
                }
            }
            if (zeroes <= m && ones <= n)
                nums.push_back({zeroes, ones});
        }

        int N = nums.size();
        std::cout << N << "\n";

        // edge case
        if (N == 0)
            return 0;

        vector<vector<vector<int>>> dp(N, vector<vector<int>>(m + 1, vector<int>(n + 1, 0)));

        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    if (i > 0) {
                        if (j >= nums[i].first && k >= nums[i].second) {
                            dp[i][j][k] = max(
                                dp[i-1][j][k], 
                                1 + dp[i-1][j-nums[i].first][k-nums[i].second]
                            );
                        } else {
                            dp[i][j][k] = dp[i-1][j][k];
                        }  
                    } else {
                        dp[i][j][k] = (j >= nums[i].first && k >= nums[i].second) ? 1 : 0;
                    }
                    // std::cout << i << " " << j << " " << k << " : " << dp[i][j][k] << "\n";                
                }
            }
        }

        return dp[N-1][m][n];
    
    }
};