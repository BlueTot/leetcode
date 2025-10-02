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

        // for (int i = 0; i < matches.size(); i++) {
        //     std::cout << matches[i] << ", ";
        // }
        // std::cout << "\n";

        vector<vector<bool>> dp(
            s.size() + 1,
            vector<bool>(matches.size() + 1, false)
        );
        dp[0][0] = true;
        for (int j = 0; j < matches.size(); j++) {
            if (matches[j].size() == 1) { // character
                dp[0][j+1] = false;
            } else { // star
                dp[0][j+1] = dp[0][j];
            }
        }

        for (int i = 0; i < s.size(); i++) {
            for (int j = 0; j < matches.size(); j++) {
                if (matches[j].size() == 1) { // character
                    dp[i+1][j+1] = (
                        s[i] == matches[j][0] || matches[j][0] == '.'
                    ) && dp[i][j];
                } else { // star
                    dp[i+1][j+1] = dp[i][j+1] && (
                        matches[j][0] == s[i] || matches[j][0] == '.'
                    ) || dp[i+1][j];
                }
            }
        }

        for (int i = 0; i < dp.size(); i++) {
            for (int j = 0; j < dp[0].size(); j++) {
                std::cout << dp[i][j] << ", ";
            }
            std::cout << "\n";
        }

        return dp[s.size()][matches.size()];
    }
};