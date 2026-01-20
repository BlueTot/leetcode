class Solution {
public:
    int singleNumber(vector<int>& nums) {

        // the idea is that we maintain a vector of the number of set bits in each position
        // if the number of set bits in total is 1 mod 3, then that bit must be set in the result number
        // we find the set bits to reconstruct the result number
        
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

        int res = 0;
        for (int i = positions.size()-1; i >= 0; i--) {
            res += (positions[i] % 3);
            if (i > 0)
                res <<= 1;
        }

        return res;
    }
};