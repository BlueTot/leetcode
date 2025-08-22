# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        array = []
        self.__flatten(root, array)
        curr = root
        for i, val in enumerate(array):
            curr.val = val
            curr.left = None
            if (i != len(array)-1):
                curr.right = TreeNode()
            curr = curr.right
    
    def __flatten(self, curr, array):
        if curr == None: return
        array.append(curr.val)
        self.__flatten(curr.left, array)
        self.__flatten(curr.right, array)
        