class Solution {
public:
    int singleNumber(vector<int>& nums) {
        
        vector<int> positions(32, 0);
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int j = 0;
            while (num != 0 && j < 32) {
                positions[j] += num & 1;
                num >>= 1;
                j++;
            }
        }

        // for (int i = 0; i < positions.size(); i++) {
        //     cout << positions[i] << "\n";
        // }

        int res = 0;
        for (int i = positions.size()-1; i >= 0; i--) {
            res += (positions[i] % 3);
            if (i > 0)
                res <<= 1;
        }

        return res;
    }
};