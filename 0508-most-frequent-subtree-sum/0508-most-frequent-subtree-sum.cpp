#include <limits>

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

    int subtreeSum(TreeNode* node, unordered_map<int, int> &counter) {
        if (node == NULL)
            return 0;
        
        int sum = node->val;
        if (node->left != NULL)
            sum += subtreeSum(node->left, counter);
        if (node->right != NULL)
            sum += subtreeSum(node->right, counter);

        counter[sum]++;
        return sum;
    }

    vector<int> findFrequentTreeSum(TreeNode* root) {
        
        unordered_map<int, int> counter;
        subtreeSum(root, counter);

        int largest = std::numeric_limits<int>::min();
        for (auto& pair: counter) {
            largest = max(largest, pair.second);
        }

        vector<int> res;
        for (auto& pair: counter) {
            if (pair.second == largest)
                res.push_back(pair.first);
        }

        return res;
    }
};