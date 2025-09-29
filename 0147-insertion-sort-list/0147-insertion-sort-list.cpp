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
    ListNode* insertionSortList(ListNode* head) {
        
        ListNode* first = head;
        ListNode* new_head = head;
        ListNode* prev_node = head;

        // we start insertion sort at second node.
        first = first->next;
        
        while (first != NULL) {

            ListNode* next_node = first->next; // store the next node
            ListNode* curr = new_head; // current moving pointer
            ListNode* prev = NULL; // previous of the curr

            // advance until we find a spot
            while (curr != first && first->val > curr->val) {
                prev = curr;
                curr = curr->next;
            }

            // if we didn't find a spot, then the list is in order.
            if (curr == first) {
                first = next_node;
                prev_node = curr;
                continue;
            }
            
            // slot in at the start
            if (prev == NULL) {
                first->next = curr; // connect first up to the chain
                prev_node->next = next_node; // update to skip removed node
                new_head = first; // update head

            } else {
                first->next = curr; // connect up to curr
                prev->next = first; // connect prev up
                prev_node->next = next_node;
                // if (curr->next == first) { // if next node is the node that's removed
                //     curr->next = next_node; // skip past it
                //     prev_node = curr;
                // } else {
                //     prev_node->next = next_node;
                // }

            }

            first = next_node;

        }

        return new_head;
    }
};