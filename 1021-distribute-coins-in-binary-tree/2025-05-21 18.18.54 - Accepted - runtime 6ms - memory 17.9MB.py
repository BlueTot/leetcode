# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        def distribute(node) -> (int, int):
            if node == None:
                return 0, 0
            amount1, move1 = distribute(node.left)
            node.val -= amount1
            amount2, move2 = distribute(node.right)
            node.val -= amount2
            return (1 - node.val, move1+move2+abs(amount1)+abs(amount2))
        
        return distribute(root)[1]
            