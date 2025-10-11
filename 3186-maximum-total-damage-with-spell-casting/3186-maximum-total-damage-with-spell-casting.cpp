class Solution {
public:
    long long maximumTotalDamage(vector<int>& power) {
        
        unordered_map<int, int> counter;
        for (int damage : power)
            counter[damage]++;
        
        vector<int> unique;
        for (auto pair : counter) 
            unique.push_back(pair.first);
        sort(unique.begin(), unique.end());

        vector<long long> dp(unique.size(), 0);
        long long largest = 0LL;

        for (int i = 0; i < dp.size(); i++) {

            int left = 0;
            int right = dp.size() - 1;
            while (left < right) {
                int mid = (left + right) / 2;
                if (unique[mid] >= unique[i] - 2)
                    right = mid;
                else
                    left = mid + 1;
            }

            // cout << i << " " << left-1 << "\n";

            // best valid index is now left - 1
            if (left - 1 >= 0)
                dp[i] = max(dp[left-1] + (long long) unique[i] * counter[unique[i]], dp[i-1]);
            else if (i > 0)
                dp[i] = max(dp[i-1], (long long) unique[i] * counter[unique[i]]);
            else
                dp[i] = (long long) unique[i] * counter[unique[i]];
            largest = max(largest, dp[i]);
            
            // cout << dp[i] << ", ";

        }

        // cout << "\n";
        return largest;

    }
};