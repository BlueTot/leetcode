# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.__stack = []
        self.__pushAllLeft(root)
    
    def __pushAllLeft(self, curr):
        while (curr != None):
            self.__stack.append(curr)
            curr = curr.left

    def next(self) -> int:
        node = self.__stack.pop()
        if (node.right != None):
            self.__pushAllLeft(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.__stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()