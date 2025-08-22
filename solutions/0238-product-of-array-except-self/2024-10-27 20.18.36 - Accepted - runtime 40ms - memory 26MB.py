class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [0]*len(nums)
        product_right = [0]*len(nums)
        product_left[0] = nums[0]
        product_right[-1] = nums[-1]
        for i in range(1, len(nums)):
            product_left[i] = product_left[i-1] * nums[i]
        for i in range(len(nums)-2, -1, -1):
            product_right[i] = product_right[i+1]*nums[i]
        products = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                products[i] = product_right[i+1]
            elif i == len(nums)-1:
                products[i] = product_left[i-1]
            else:
                products[i] = product_left[i-1] * product_right[i+1]
        return products
            
        