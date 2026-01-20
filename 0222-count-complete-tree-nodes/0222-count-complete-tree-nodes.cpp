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
    int countNodes(TreeNode* root) {

        if (root == NULL)
            return 0;

        if (root->left == NULL && root->right == NULL)
            return 1;
        
        int left_height = 0, right_height = 0;

        TreeNode* curr = root->left;
        while (curr != NULL) {
            curr = curr->left;
            left_height++;
        }

        curr = root->right;
        while (curr != NULL) {
            curr = curr->left;
            right_height++;
        }

        // cout << left_height << " " << right_height << "\n";
        // equal - left subtree is perfect
        if (left_height == right_height) {
            return (1 << left_height) + countNodes(root->right);

        // difference by 1 - right subtree is perfect
        } else {
            return (1 << right_height) + countNodes(root->left);
        }
    }
};