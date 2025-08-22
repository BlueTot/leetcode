class Solution {
public:
    int tribonacci(int n) {
        int trinums[40];
        trinums[0] = 0;
        trinums[1] = 1;
        trinums[2] = 1;
        for (int i = 3;i <= n; i++){
            trinums[i] = trinums[i-3] + trinums[i-2] + trinums[i-1];
        }
        return trinums[n];
                }

    };