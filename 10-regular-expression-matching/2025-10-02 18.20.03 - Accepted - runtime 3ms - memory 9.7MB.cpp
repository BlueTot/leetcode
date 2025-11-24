class Solution {
public:

    vector<string> parsePattern(string p) {
        vector<string> matches;
        int i = 0;
        while (i < p.size()) {
            if (i < p.size() - 1 && p[i+1] == '*') {
                matches.push_back(p.substr(i, 2));
                i += 2;
            } else {
                matches.push_back(p.substr(i, 1));
                i++;
            }
        }
        return matches;
    }

    bool isMatch(string s, string p) {
        
        vector<string> matches = parsePattern(p);

        vector<vector<bool>> dp(
            s.size() + 1,
            vector<bool>(matches.size() + 1, false)
        );

        dp[0][0] = true; // empty string, empty match is ok

        for (int j = 0; j < matches.size(); j++) {
            if (matches[j].size() == 1) {
                dp[0][j+1] = false; // character does not match empty string
            } else { 
                dp[0][j+1] = dp[0][j]; // star matches if the previous match was successful
            }
        }

        for (int i = 0; i < s.size(); i++) {
            for (int j = 0; j < matches.size(); j++) {
                if (matches[j].size() == 1) { // character
                    /* character matches if we have either the character or wildcard, 
                    and the previous match is successful */
                    dp[i+1][j+1] = (
                        s[i] == matches[j][0] || matches[j][0] == '.'
                    ) && dp[i][j];
                } else { // star
                    /* star matches if ignoring the star matches (0), 
                    or the star match extends to the current character (1+) */
                    dp[i+1][j+1] = dp[i][j+1] && (
                        matches[j][0] == s[i] || matches[j][0] == '.'
                    ) || dp[i+1][j];
                }
            }
        }

        return dp[s.size()][matches.size()];
    }
};