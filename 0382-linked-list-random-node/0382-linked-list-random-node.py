# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from random import randint

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.__values = []
        while (head != None):
            self.__values.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        index = randint(0, len(self.__values) - 1)
        return self.__values[index]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()