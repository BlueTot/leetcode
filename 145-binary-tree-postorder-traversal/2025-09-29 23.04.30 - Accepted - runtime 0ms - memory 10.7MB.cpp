/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        
        vector<pair<TreeNode*, int>> stack;
        stack.push_back({root, 0});
        vector<int> result;
        TreeNode* node;

        while (stack.size() > 0) {

            auto pair = stack.back();
            if (pair.first == NULL) {
                stack.pop_back();
                continue;
            }

            if (pair.second == 0) {
                stack.back().second++;
                stack.push_back({pair.first->left, 0});
                
            } else if (pair.second == 1) {
                stack.back().second++;
                stack.push_back({pair.first->right, 0});

            } else if (pair.second == 2) {
                stack.back().second++; 
                result.push_back(pair.first->val);
                
            } else {
                stack.pop_back();
            }    
        }

        return result;

    }
};