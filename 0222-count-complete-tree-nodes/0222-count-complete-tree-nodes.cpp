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

        // idea is that one of the subtrees will be perfect, one isnt
        // we can test by checking the heights of the subtrees
        // once we know which is perfect, if its height is h, the number of nodes
        // in the subtree is 2^(h+1)-1. And we can add on the root node, and recurse to the
        // imperfect subtree

        // we make log(n) recursive calls, each level we perform log(n) work so it is
        // log(n)^2 time complexity

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

        // equal - left subtree is perfect
        if (left_height == right_height) {
            return (1 << left_height) + countNodes(root->right);

        // difference by 1 - right subtree is perfect
        } else {
            return (1 << right_height) + countNodes(root->left);
        }
    }
};