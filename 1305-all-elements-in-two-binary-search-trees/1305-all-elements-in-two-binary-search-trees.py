# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        
        def in_order(root: Optional[TreeNode]) -> List[int]:
            if root is None:
                return []
            res = in_order(root.left)
            res.append(root.val)
            res.extend(in_order(root.right))
            return res
        
        arr1, arr2 = in_order(root1), in_order(root2)
        res = []
        i, j = 0, 0

        while (i < len(arr1) and j < len(arr2)):
            if arr1[i] <= arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        
        while (i < len(arr1)):
            res.append(arr1[i])
            i += 1
        
        while (j < len(arr2)):
            res.append(arr2[j])
            j += 1
        
        return res
