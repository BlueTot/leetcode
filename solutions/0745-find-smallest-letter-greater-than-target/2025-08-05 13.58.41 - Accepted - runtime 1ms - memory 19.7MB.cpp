class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int left = 0;
        int right = letters.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            cout << left << " " << right << " " << mid << "\n";
            if (mid > 0 && letters.at(mid-1) <= target && letters.at(mid) > target) {
                return letters.at(mid);
            } else if (letters.at(mid) <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return letters.at(0);
    }
};