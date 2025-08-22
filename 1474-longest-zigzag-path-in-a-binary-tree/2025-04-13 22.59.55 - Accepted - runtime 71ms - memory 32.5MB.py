# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __longest(self, curr) -> int:
        if curr == None:
            return -1, -1
        left = 1 + self.__longest(curr.left)[1]
        right = 1 + self.__longest(curr.right)[0]
        self.__max = max(self.__max, left, right)
        return (left, right)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.__max = 0
        self.__longest(root)
        return self.__max