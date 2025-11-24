/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNodes(ListNode* head) {

        /* determine values to remove */
        
        stack<ListNode*> mstack;
        unordered_set<ListNode*> node_set;

        ListNode* curr = head;
        while (curr != NULL) {
            while (!mstack.empty() && mstack.top()->val < curr->val) {
                node_set.insert(mstack.top());
                mstack.pop();
            }
            mstack.push(curr);
            curr = curr->next;
        }

        /* code for removing values from linked list */
        
        curr = head;

        while (curr->next != NULL) {
            if (node_set.contains(curr->next)) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }

        if (node_set.contains(head)) {
            head = head->next;
        }

        return head;

    }
};