class Solution {
public:
    int rob(vector<int>& nums) {

        /* case nums is length 1 */
        if (nums.size() == 1)
            return nums[0];

        /* maximum in the range l to r not inclusive */
        auto max_range = [&](int l, int r) {
            int res = 0;
            int first = 0, second = 0, temp = 0;
            for (int i = l; i < r; i++) {
                if (i == l) {
                    first = nums[i];
                } else if (i == l + 1) {
                    second = max(first, nums[i]);
                } else {
                    temp = max(second, nums[i] + first);
                    first = second;
                    second = temp;
                }
                res = max(res, max(first, second));
            }
            return res;
        };

        /* we can either rob 0 to n-2, or 1 to n-1
           because we can't rob houses 0 and n-1 at the same time*/
        return max(max_range(0, nums.size()-1), max_range(1, nums.size()));

    }
};