class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        unordered_set<int> nums_set;
        for (int num : nums)
            nums_set.insert(num);

        return nums_set.size() != nums.size();
    }
};