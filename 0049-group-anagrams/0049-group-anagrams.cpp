class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> map;
        string k;
        for (string s : strs) {
            k = s;
            sort(k.begin(), k.end());
            map[k].push_back(s);
        }

        vector<vector<string>> result;
        for (auto pair : map) {
            result.push_back(pair.second);
        }

        return result;
    }
};