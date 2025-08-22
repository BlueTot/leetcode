class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProduct = -float("inf")
        currProduct = [1, 1]
        for num in nums:

            newProduct = [0, 0]
            smallest, largest = min(currProduct), max(currProduct)

            if num >= 0:
                if largest >= 0:
                    newProduct[0] = largest * num
                else:
                    newProduct[0] = num
            else:
                if smallest < 0:
                    newProduct[0] = smallest * num
                else:
                    newProduct[0] = num

            if num >= 0:
                if smallest < 0:
                    newProduct[1] = smallest * num
                else:
                    newProduct[1] = num
            else:
                if largest > 0:
                    newProduct[1] = largest * num
                else:
                    newProduct[1] = num
            
            currProduct = newProduct
            maxProduct = max(maxProduct, max(*currProduct))
        
        return maxProduct
