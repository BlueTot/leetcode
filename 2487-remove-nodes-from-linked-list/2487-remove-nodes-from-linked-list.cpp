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
        
        stack<int> mstack;
        unordered_set<int> removes;

        ListNode* curr = head;
        while (curr != NULL) {
            while (!mstack.empty() && mstack.top() < curr->val) {
                removes.insert(mstack.top());
                mstack.pop();
            }
            mstack.push(curr->val);
            curr = curr->next;
        }

        /* code for removing values from linked list */
        
        curr = head;

        while (curr->next != NULL) {
            if (removes.contains(curr->next->val)) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }

        if (removes.contains(head->val)) {
            head = head->next;
        }
        
        return head;

    }
};