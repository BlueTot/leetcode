class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        
        int m = grid.size(), n = grid[0].size();
        if (m < 3 || n < 3)
            return 0;
    
        unordered_set<int> nums;

        auto check = [&](int i, int j) {

            // add to set and check if there are 9 elements
            nums.clear();

            for (int di = 0; di < 3; di++) {
                for (int dj = 0; dj < 3; dj++) {
                    if (grid[i+di][j+dj] > 9 || grid[i+di][j+dj] < 1)
                        return false;
                    nums.insert(grid[i+di][j+dj]);
                }
            }

            if (nums.size() != 9)
                return false;
            
            // check sums are equal
            int r1 = grid[i][j] + grid[i][j+1] + grid[i][j+2];
            int r2 = grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2];
            int r3 = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2];

            int c1 = grid[i][j] + grid[i+1][j] + grid[i+2][j];
            int c2 = grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1];
            int c3 = grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2];

            int d1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2];
            int d2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2];

            return (r1 == r2 && r2 == r3 && r3 == c1 && c1 == c2 && 
                    c2 == c3 && c3 == d1 && d1 == d2);
        };

        int count = 0;

        for (int i = 0; i < m-2; i++) {
            for (int j = 0; j < n-2; j++) {
                if (check(i, j))
                    count++;
            }
        }

        return count;

    }
};