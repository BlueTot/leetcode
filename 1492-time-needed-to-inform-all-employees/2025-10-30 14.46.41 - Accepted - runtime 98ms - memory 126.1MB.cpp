class Solution {
public:

    int time(vector<vector<int>>& children, vector<int>& informTime, int node) {
        int largest = 0;
        for (int child : children[node]) {
            largest = max(largest, time(children, informTime, child));
        }
        return informTime[node] + largest;
    }

    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        
        vector<vector<int>> children(n);
        for (int i = 0; i < n; i++) {
            if (manager[i] != -1)
                children[manager[i]].push_back(i);
        }

        return time(children, informTime, headID);
        
    }
};