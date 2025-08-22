# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __pathSum(self, curr, targetSum, path, total):
        if curr.left == None and curr.right == None and total == targetSum:
            return [path]
        paths = []
        if curr.left is not None:
            paths.extend(self.__pathSum(curr.left, targetSum, path+[curr.left.val], total+curr.left.val))
        if curr.right is not None:
            paths.extend(self.__pathSum(curr.right, targetSum, path+[curr.right.val], total+curr.right.val))
        return paths

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        return self.__pathSum(root, targetSum, [root.val], root.val)