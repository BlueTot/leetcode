class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {

        int n = (int) grid.size();
        int m = (int) grid[0].size();
        vector<vector<bool>> seen(n, vector<bool>(m, false));

        auto in_bounds = [&](int r, int c) {
            return 0 <= r && r < n && 0 <= c && c < m;
        };
        
        auto bfs = [&](int sr, int sc) {

            int area = 0;
            queue<pair<int, int>> q;
            q.push({sr, sc});
            
            while (!q.empty()) {
                auto [r, c] = q.front(); q.pop();
                if (seen[r][c]) continue;
                seen[r][c] = true;
                area++;

                static const int dr[4] = {-1, 1, 0, 0};
                static const int dc[4] = {0, 0, -1, 1};
                for (int k = 0; k < 4; k++) {
                    int nr = r + dr[k], nc = c + dc[k];
                    if (in_bounds(nr, nc) && grid[nr][nc])
                        q.push({nr, nc});
                }
            }

            return area;
        };

        int best = 0;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                if (grid[r][c] && !seen[r][c])
                    best = max(best, bfs(r, c));
                else
                    seen[r][c] = true;
            }
        }

        return best;
    }
};
