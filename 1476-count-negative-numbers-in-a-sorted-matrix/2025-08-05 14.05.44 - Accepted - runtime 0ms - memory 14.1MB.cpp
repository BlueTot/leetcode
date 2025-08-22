class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int r = grid.size() - 1;
        int c = 0;
        int numPos = 0;
        while (r >= 0 && c < grid[0].size()) {
            if (grid[r][c] < 0) {
                numPos += c;
                r--;
            } else {
                c++;
            }
        }
        if (r >= 0) numPos += c * (r + 1); // condition at top
        return grid.size() * grid[0].size() - numPos;
    }
};