/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:

    bool hasCycle(ListNode *&fast, ListNode *slow) {
        while (fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow)
                return true; 
        }
        return false;
    }

    ListNode *detectCycle(ListNode *head) {
        
        ListNode *fast = head;
        ListNode *slow = head;

        if (!hasCycle(fast, slow))
            return NULL;
        
        while (fast != slow) {
            fast = fast->next;
            slow = slow->next;
        }

        return slow;
    }
};