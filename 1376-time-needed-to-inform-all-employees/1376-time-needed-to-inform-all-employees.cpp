class Solution {
public:

    int time(unordered_map<int, vector<int>>& children, vector<int>& informTime, int node) {
        int largest = 0;
        for (int child : children[node]) {
            largest = max(largest, time(children, informTime, child));
        }
        return informTime[node] + largest;
    }

    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        
        unordered_map<int, vector<int>> children;
        for (int i = 0; i < n; i++) {
            children[manager[i]].push_back(i);
        }

        return time(children, informTime, headID);
        
    }
};