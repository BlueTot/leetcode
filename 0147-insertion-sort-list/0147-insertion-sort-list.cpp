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

            ListNode* curr2 = new_head;
            // while (curr2 != NULL) {
            //     std::cout << curr2->val << ", ";
            //     curr2 = curr2->next;
            // }
            // std::cout << "\n";
            // std::cout << (first != NULL ? first->val : NULL) << "\n";
            // std::cout << new_head->val << "\n";
            // std::cout << prev_node->val << "\n";

            ListNode* next_node = first->next;
            ListNode* curr = new_head;
            ListNode* prev = NULL;

            // advance until we find a spot
            while (curr != first && first->val > curr->val) {
                prev = curr;
                curr = curr->next;
            }

            if (curr == first) {
                first = next_node;
                prev_node = curr;
                continue;
            }
            
            // slot in the node
            if (prev == NULL) {
                first->next = curr;
                prev_node->next = next_node;
                new_head = first;
            } else {
                // std::cout << first->val << " " << prev->val << " " << curr->val << " " << prev_node->val << "\n";
                first->next = curr;
                prev->next = first;
                if (curr->next == first) {
                    curr->next = next_node;
                    prev_node = curr;
                } else {
                    prev_node->next = next_node;
                }
            }

            first = next_node;

        }

        return new_head;
    }
};