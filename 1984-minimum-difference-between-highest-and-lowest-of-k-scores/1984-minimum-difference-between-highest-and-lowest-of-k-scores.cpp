class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        
        if (k == 1) {
            return 0;
        }

        // sort the numbers so they are in non-decreasing order
        sort(nums.begin(), nums.end());

        int diff = 1 << 30;

        // compare differences nums[i+k-1] - nums[i] for all valid i.
        // this is equivalent to looking at a sliding window of size k
        
        for (int i = 0; i < nums.size() - k + 1; i++) {
            diff = min(diff, nums[i+k-1] - nums[i]);
        }

        return diff;

    }
};