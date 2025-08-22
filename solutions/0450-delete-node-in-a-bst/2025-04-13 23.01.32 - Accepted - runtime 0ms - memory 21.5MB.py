# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.__delete(root, key)

    def __maxValue(self, curr):
        if curr.right is not None:
            return self.__maxValue(curr.right)
        else:
            return curr.val
        
    def __delete(self, curr, key):
        if curr == None:
            return curr
        
        if key < curr.val:
            curr.left = self.__delete(curr.left, key)
        elif key > curr.val:
            curr.right = self.__delete(curr.right, key)
        else:
            if curr.left is None and curr.right is None: # case 1
                return None
            elif curr.left is not None and curr.right is None: # case 2a
                return curr.left
            elif curr.left is None and curr.right is not None: # case 2b
                return curr.right
            else: # case 3
                maxValue = self.__maxValue(curr.left)
                curr.left = self.__delete(curr.left, maxValue)
                curr.val = maxValue
        
        return curr
