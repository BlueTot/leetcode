class Solution {
public:
    vector<string> generateParenthesis(int n) {
        
        if (n == 0)
            return {""};
        if (n == 1)
            return {"()"};
        
        vector<string> output;
        for (int i = 0; i < n; i++) {
            for (string inner : generateParenthesis(i)) {
                for (string remaining : generateParenthesis(n-i-1)) {
                    output.push_back("(" + inner + ")" + remaining);
                }
            }
        }
        
        return output;

    }
};