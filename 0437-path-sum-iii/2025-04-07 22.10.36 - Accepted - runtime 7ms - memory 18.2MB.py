# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.__pathSum(root, targetSum, 0, {0 : 1})
        
    
    def __pathSum(self, curr, k, prefixSum, counter):
        
        if curr == None:
            return 0
        
        paths = 0
        prefixSum += curr.val
        if prefixSum - k in counter:
            paths += counter[prefixSum - k]
        counter[prefixSum] = counter.get(prefixSum, 0) + 1
        paths += self.__pathSum(curr.left, k, prefixSum, counter)
        paths += self.__pathSum(curr.right, k, prefixSum, counter)
        counter[prefixSum] = counter[prefixSum] - 1

        return paths
