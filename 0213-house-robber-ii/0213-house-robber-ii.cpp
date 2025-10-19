class Solution {
public:
    int rob(vector<int>& nums) {

        /* case nums is length 1 */
        if (nums.size() == 1)
            return nums[0];
        
        /* we can either rob houses 0 to n-2 */
        int max1 = 0;
        vector<int> dp1(nums.size(), 0);
        for (int i = 0; i < nums.size() - 1; i++) {
            if (i == 0) {
                dp1[i] = nums[i];
            } else if (i == 1) {
                dp1[i] = max(dp1[i-1], nums[i]);
            } else {
                dp1[i] = max(dp1[i-1], nums[i] + dp1[i-2]);
            }
            max1 = max(max1, dp1[i]);
        }

        /* or rob houses 1 to n-1 */
        int max2 = 0;
        vector<int> dp2(nums.size(), 0);
        for (int i = 1; i < nums.size(); i++) {
            if (i == 1) {
                dp2[i] = nums[i];
            } else if (i == 2) {
                dp2[i] = max(dp2[i-1], nums[i]);
            } else {
                dp2[i] = max(dp2[i-1], nums[i] + dp2[i-2]);
            }
            max2 = max(max2, dp2[i]);
        }

        return max(max1, max2);

    }
};