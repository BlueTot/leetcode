class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> ransomCounter;
        for (const auto& c : ransomNote) {
            ransomCounter[c]++;
        }
        unordered_map<char, int> magazineCounter;
        for (const auto& c : magazine) {
            magazineCounter[c]++;
        }
        for (const auto& pair : ransomCounter) {
            if (magazineCounter[pair.first] < pair.second)
                return false;
        }
        return true;
    }
};