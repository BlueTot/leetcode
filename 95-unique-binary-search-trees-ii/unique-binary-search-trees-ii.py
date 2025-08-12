# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def trees(nums : Tuple[int]) -> List[Optional[TreeNode]]:
            if len(nums) == 0:
                return [None]
            if len(nums) == 1:
                return [TreeNode(nums[0])]
            if len(nums) == 2:
                smaller, larger = min(nums), max(nums)
                return [
                    TreeNode(val=larger, left=TreeNode(smaller)),
                    TreeNode(val=smaller, right=TreeNode(larger))
                ]
            result = []
            for i in range(len(nums)):
                for left in trees(nums[:i]):
                    for right in trees(nums[i+1:]):
                        result.append(TreeNode(
                            val=nums[i],
                            left=left,
                            right=right
                        ))
            return result
        
        return trees(tuple(i for i in range(1, n+1)))
                