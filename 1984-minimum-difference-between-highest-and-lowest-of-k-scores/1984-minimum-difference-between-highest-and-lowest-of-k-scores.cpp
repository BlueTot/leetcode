class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        
        if (k == 1) {
            return 0;
        }

        sort(nums.begin(), nums.end());

        int diff = 1 << 30;
        for (int i = 0; i < nums.size() - k + 1; i++) {
            diff = min(diff, nums[i+k-1] - nums[i]);
        }

        return diff;

    }
};