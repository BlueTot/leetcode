class Solution {
public:
    bool checkStrings(string s1, string s2) {

        vector<int> odd(26, 0), even(26, 0);
        
        for (int i = 0; i < s1.size(); i++) {
            char c = s1[i];
            if (i % 2 == 0) {
                even[c - 'a']++;
            } else {
                odd[c - 'a']++;
            }
        }

        for (int i = 0; i < s2.size(); i++) {
            char c = s2[i];
            if (i % 2 == 0){
                if (even[c - 'a'] == 0)
                    return false;
                even[c - 'a']--;
            } else {
                if (odd[c - 'a'] == 0)
                    return false;
                odd[c - 'a']--;
            }
        }

        return true; 
    }
};