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

    unordered_map<TreeNode*, int> heights;

public:
    bool isBalanced(TreeNode* root) {

        if (root == NULL)
            return true;

        if (root->left == NULL && root->right == NULL) {
            heights[root] = 0;
            return true;
        }

        if (!isBalanced(root->left) || !isBalanced(root->right))
            return false;
            
        int h1 = (root->left == NULL) ? -1 : heights[root->left];
        int h2 = (root->right == NULL) ? -1 : heights[root->right];

        int h = 1 + std::max(h1, h2);
        heights[root] = h;

        return std::abs(h1 - h2) <= 1;     
    }
};