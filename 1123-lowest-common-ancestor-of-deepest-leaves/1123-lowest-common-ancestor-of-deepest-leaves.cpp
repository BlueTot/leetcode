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
    TreeNode* lcaDeepestLeaves(TreeNode* root) {

        deque<pair<TreeNode*, int>> queue;
        queue.push_back({root, 0});

        int max_depth = 0;
        vector<pair<TreeNode*,int>> leaves;

        unordered_map<TreeNode*, TreeNode*> parent;
        parent.insert({root, nullptr});

        while (!queue.empty()) {
            auto [node, depth] = queue.front(); queue.pop_front();
            if (node->left == nullptr && node->right == nullptr) {
                max_depth = max(max_depth, depth);
                leaves.push_back({node, depth});
            }
            if (node->left != nullptr) {
                queue.push_back({node->left, depth + 1});
                parent.insert({node->left, node});
            }   
            if (node->right != nullptr) {
                queue.push_back({node->right, depth + 1});
                parent.insert({node->right, node});
            }  
        }

        deque<TreeNode*> queue2;

        for (auto pair : leaves) {
            if (pair.second == max_depth)
                queue2.push_back(pair.first);     
        }

        unordered_set<TreeNode*> seen;

        while (queue2.size() > 1) {
            TreeNode* node = queue2.front(); queue2.pop_front();
            TreeNode* p = parent.at(node);
            if (p != nullptr && !seen.contains(p)) {
                seen.insert(p);
                queue2.push_back(parent.at(node));
            }
        }

        return queue2.front();
        
    }
};