/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        
        vector<vector<Node*>> levels;
        deque<pair<Node*, int>> queue;
        queue.push_back({root, 0});

        while (!queue.empty()) {

            auto [curr, level] = queue.front(); queue.pop_front();

            if (curr == NULL)
                continue;

            if (curr->left != NULL)
                queue.push_back({curr->left, level+1});
            if (curr->right != NULL)
                queue.push_back({curr->right, level+1});
            
            if (level >= levels.size())
                levels.push_back(vector<Node*>());
            levels[level].push_back(curr); 

        }

        for (int i = 0; i < levels.size(); i++) {
            for (int j = 0; j < levels[i].size(); j++) {
                if (j < levels[i].size() - 1)
                    levels[i][j]->next = levels[i][j+1];
                else
                    levels[i][j]->next = NULL;
            }
        }

        return root;

    }
};