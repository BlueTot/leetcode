class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        # find the rotation amount
        amount = 0
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            print(left, right, mid)
            if nums[mid] > nums[(mid+1)%len(nums)]:
                amount = mid + 1
                break
            elif nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        print(amount)
        # find the index given we know the shift amount
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            actual = (mid + amount) % len(nums)
            if target == nums[actual]:
                return actual
            elif target < nums[actual]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1
