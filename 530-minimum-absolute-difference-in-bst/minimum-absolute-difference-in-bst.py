# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def inOrder(node):
            if node == None:
                return []
            output = []
            output.extend(inOrder(node.left))
            output.append(node.val)
            output.extend(inOrder(node.right))
            return output
        
        vals = inOrder(root)
        minDist = float("inf")
        for i in range(len(vals)-1):
            minDist = min(minDist, vals[i+1] - vals[i])
        return minDist