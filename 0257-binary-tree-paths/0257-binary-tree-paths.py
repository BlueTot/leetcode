# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        # base cases
        if root is None:
            return [""]
        if root.left is None and root.right is None:
            return [f"{root.val}"]

        res = []
        if root.left is not None:
            for path in self.binaryTreePaths(root.left):
                res.append(f"{root.val}->{path}")

        if root.right is not None:
            for path in self.binaryTreePaths(root.right):
                res.append(f"{root.val}->{path}")
        
        return res