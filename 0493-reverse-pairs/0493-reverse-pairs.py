class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        def reverse(nums: List[int]) -> tuple[List[int], int]:

            # base cases
            if len(nums) == 1:
                return (nums, 0)

            if len(nums) == 2:
                res = [nums[1], nums[0]] if nums[0] > nums[1] else nums
                count = 1 if nums[0] > 2 * nums[1] else 0
                return (res, count)

            # recurse
            mid = len(nums) // 2
            left, left_count = reverse(nums[:mid])
            right, right_count = reverse(nums[mid:])

            # merge counts
            r, count = 0, 0
            for l in range(0, len(left)):
                while (r < len(right) and left[l] > 2 * right[r]):
                    r += 1
                count += r
            
            # print(left, right, left_count, right_count, count)
            
            # merge arrays
            res = []
            i, j = 0, 0
            while (i < len(left) and j < len(right)):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            while (i < len(left)):
                res.append(left[i])
                i += 1

            while (j < len(right)):
                res.append(right[j])
                j += 1
            
            return res, left_count + right_count + count

        return reverse(nums)[1]