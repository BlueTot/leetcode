class Solution {
public:
    int mincostTickets(vector<int>& days, vector<int>& costs) {

        const vector<int> intervals = {1, 7, 30};
        
        auto find_next_greatest = [&](int bound) {
            int left = 0, right = days.size(), mid;
            while (left < right) {
                mid = (left + right) / 2;
                if (days[mid] >= bound) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }
            return left;
        };
        
        vector<int> dp(days.size(), 0);
        for (int i = days.size()-1; i >= 0; i--) {
            int res = 1 << 30;
            for (int j = 0; j < costs.size(); j++) {
                int next_idx = find_next_greatest(days[i] + intervals[j]);
                res = min(res, costs[j] + (next_idx < days.size() ? dp[next_idx] : 0));
            }
            dp[i] = res;
        }

        return dp[0];
    }
};