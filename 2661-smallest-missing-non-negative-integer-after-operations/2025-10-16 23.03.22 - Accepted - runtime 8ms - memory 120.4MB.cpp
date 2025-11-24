class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        
        auto mod = [](int a, int b) {
            return ((a % b) + b) % b;
        };

        vector<int> mods(value, 0);
        for (int num : nums) {
            mods[mod(num, value)]++;
        }

        int min_count = *min_element(mods.begin(), mods.end());
        int result = value * min_count;
        for (int i = 0; i < value; i++) {
            if (mods[i] == min_count) {
                result += i;
                break;
            }
        }

        return result;
    }
};