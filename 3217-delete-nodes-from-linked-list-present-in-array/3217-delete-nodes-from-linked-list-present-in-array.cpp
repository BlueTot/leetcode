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
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        
        unordered_set<int> nums_set;
        for (int num : nums)
            nums_set.insert(num);
        
        ListNode* curr = head;

        while (curr->next != NULL) {
            if (nums_set.contains(curr->next->val)) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }

        if (nums_set.contains(head->val)) {
            head = head->next;
        }

        return head;
    }
};