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
    int findBottomLeftValue(TreeNode* root) {
        
        int level = 0;
        vector<int> row;
        deque<pair<TreeNode*, int>> queue;
        queue.push_back({root, 0});

        while (!queue.empty()) {
            
            auto [curr, curr_level] = queue.front(); queue.pop_front();
            if (curr_level > level) {
                row.clear();
                level++;
            }
            
            if (curr == NULL)
                continue;
            
            if (curr->left != NULL)
                queue.push_back({curr->left, curr_level + 1});
            if (curr->right != NULL)
                queue.push_back({curr->right, curr_level + 1});
            
            row.push_back(curr->val);
        }

        return row[0];

    }
};