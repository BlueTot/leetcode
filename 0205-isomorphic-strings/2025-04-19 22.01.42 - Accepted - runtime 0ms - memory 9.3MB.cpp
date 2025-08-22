class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, int> seenCharsS;
        unordered_map<char, int> seenCharsT;
        for (int i = 0; i < s.length(); i++) {
            if (seenCharsS.find(s[i]) == seenCharsS.end()) {
                seenCharsS[s[i]] = seenCharsS.size();
            }
            if (seenCharsT.find(t[i]) == seenCharsT.end()) {
                seenCharsT[t[i]] = seenCharsT.size();
            }
            if (seenCharsS[s[i]] != seenCharsT[t[i]])
                return false;
        }
        return true;
    }
};