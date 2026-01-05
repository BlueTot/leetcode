class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        
        int num_negatives = 0;
        int minimum = 10000;
        long long sum = 0;

        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] < 0)
                    num_negatives++;
                minimum = min(minimum, abs(matrix[i][j]));
                sum += abs(matrix[i][j]);
            }
        }

        if (num_negatives % 2 == 0) {
            return sum;
        } else {
            return sum - 2 * minimum;
        }
    }
};