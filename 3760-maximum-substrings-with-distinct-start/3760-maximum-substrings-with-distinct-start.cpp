class Solution {
public:
    int maxDistinct(string s) {
        unordered_set<char> chars;
        for (char s : s) {
            chars.insert(s);
        }
        return chars.size();
    }
};