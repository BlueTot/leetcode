class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        // build map of number against index
        unordered_map<int, int> indices;
        for (int i = 0; i < nums.size(); i++) {
            indices[nums[i]] = i;
        }

        // search for existing remaining
        int j, rem;
        for (int i = 0; i < nums.size(); i++) {
            rem = target - nums[i];
            if (indices.contains(rem) && (j = indices[rem]) != i)
                return {i, j};
        }

        return {};
    }
};