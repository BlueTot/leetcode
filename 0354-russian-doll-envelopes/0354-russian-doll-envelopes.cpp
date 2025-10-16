class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        
        /* sort array in non-decreasing order with first parameter first
        then second parameter. 
        we can use this to find the longest increasing sequence of heights
        given the first parameter cannot be equal, handled by fits function */

        auto compare = [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);
        };

        /* two boxes fit criteria */
        auto fits = [](const vector<int>&a, const vector<int>& b) {
            return a[0] < b[0] && a[1] < b[1];
        };

        auto print = [](const vector<int>& a) {
            cout << "[" << a[0] << ", " << a[1] << "]\n";
        };

        sort(envelopes.begin(), envelopes.end(), compare);

        for (int i = 0; i < envelopes.size(); i++) {
            print(envelopes[i]);
        }
        
        const int INF = 1 << 30;
        const int NEGINF = 1 << 31;
        vector<vector<int>> dp(envelopes.size() + 1, {INF, INF});
        dp[0] = {NEGINF, NEGINF};

        for (int i = 0; i < envelopes.size(); i++) {

            int left = 0;
            int right = dp.size() - 1;
            while (left < right) {
                int mid = (left + right) / 2;
                if (dp[mid][1] > envelopes[i][1]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }

            if (dp[left-1][1] < envelopes[i][1] && envelopes[i][1] < dp[left][1])
                dp[left] = envelopes[i];

        }

        for (int i = 0; i < dp.size(); i++) {
            print(dp[i]);
        }

        int ans = 0;
        for (int l = 0; l <= envelopes.size(); l++) {
            if (fits(dp[l], {INF, INF}))
                ans = l;
        }
        return ans;
    }
};