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
    vector<int> largestValues(TreeNode* root) {
        
        deque<pair<TreeNode*, int>> queue;
        queue.push_back({root, 0});

        int level = 0;
        int largest = 1 << 31;
        vector<int> res;

        while (!queue.empty()) {

            auto [curr, curr_level] = queue.front(); queue.pop_front();
            if (curr_level > level) {
                res.push_back(largest);
                largest = 1 << 31;
                level++;
            }

            if (curr == NULL)
                continue;
            
            if (curr->left != NULL)
                queue.push_back({curr->left, curr_level + 1});
            if (curr->right != NULL)
                queue.push_back({curr->right, curr_level + 1});
            
            largest = max(largest, curr->val);
        }

        if (root != NULL)
            res.push_back(largest);

        return res;

    }
};