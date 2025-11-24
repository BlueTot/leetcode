class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
        vector<int> dp(nums.size() + 1, 1 << 30);
        dp[0] = 1 << 31;

        for (int i = 0; i < nums.size(); i++) {

            int left = 0;
            int right = dp.size() - 1;
            while (left < right) {
                int mid = (left + right) / 2;
                if (dp[mid] > nums[i]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }

            if (dp[left-1] < nums[i] && nums[i] < dp[left])
                dp[left] = nums[i];

        }

        int res = 0;
        for (int i = 0; i < dp.size(); i++) {
            if (dp[i] < (1 << 30))
                res = i;
        }

        return res;
    }
};