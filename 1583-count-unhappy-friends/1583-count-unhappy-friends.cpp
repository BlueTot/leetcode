class Solution {
public:
    int unhappyFriends(int n, vector<vector<int>>& preferences, vector<vector<int>>& pairs) {
        
        vector<vector<int>> rank(n, vector<int>(n, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n-1; j++) {
                rank[i][preferences[i][j]] = n-j;
            }
        }

        vector<int> matching(n, 0);
        for (auto pair : pairs) {
            matching[pair[0]] = pair[1];
            matching[pair[1]] = pair[0];
        }

        int count = 0, y, v;
        for (int x = 0; x < n; x++) {
            y = matching[x];
            for (int u = 0; u < n; u++) {
                v = matching[u];
                if (rank[x][u] > rank[x][y] && rank[u][x] > rank[u][v]) {
                    count++;
                    break;
                }
            }
        }

        return count;
    }
};