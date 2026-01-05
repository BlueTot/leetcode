class Solution {
public:
    int numOfWays(int n) {

        const int M = 1000000007;
        
        vector<vector<vector<vector<int>>>> dp(n, vector<vector<vector<int>>>(3, vector<vector<int>>(3, vector<int>(3, 0))));

        int poss[12][3] = {{0, 1, 0}, {1, 0, 1}, {2, 0, 1}, {0, 1, 2}, {1, 0, 2}, {2, 0, 2}, {0, 2, 0}, {1, 2, 0}, {2, 1, 0}, {0, 2, 1}, {1, 2, 1}, {2, 1, 2}};

        for (int i = 0; i < 12; i++) {
            dp[0][poss[i][0]][poss[i][1]][poss[i][2]] = 1;
        }

        for (int i = 1; i < n; i++) {

            for (int p = 0; p < 12; p++) {

                int c1 = poss[p][0], c2 = poss[p][1], c3 = poss[p][2];

                for (int q = 0; q < 12; q++) {
                    
                    int pc1 = poss[q][0], pc2 = poss[q][1], pc3 = poss[q][2];

                    if (c1 != pc1 && c2 != pc2 && c3 != pc3)
                        dp[i][c1][c2][c3] = (dp[i][c1][c2][c3] + dp[i-1][pc1][pc2][pc3]) % M;
                }
            }

        }

        int res = 0;
        for (int i = 0; i < 12; i++) {
            res = (res + dp[n-1][poss[i][0]][poss[i][1]][poss[i][2]]) % M;
        }

        return res % M;
        
    }
};