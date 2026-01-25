class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {

        vector<int> incoming(n+1, 0), outgoing(n+1, 0);
        for (auto pair : trust) {
            incoming[pair[1]]++;
            outgoing[pair[0]]++;
        }
        
        for (int i = 1; i <= n; i++) {
            if (incoming[i] == n - 1 && outgoing[i] == 0) {
                return i;
            }
        }

        return -1;
    }
};