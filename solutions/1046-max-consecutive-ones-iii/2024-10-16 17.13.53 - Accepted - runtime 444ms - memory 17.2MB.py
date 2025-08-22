class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, j = 0, -1
        num_zeroes = k
        max_length = 0
        while j < len(nums) - 1:
            if nums[j+1] == 0 and num_zeroes > 0:
                num_zeroes -= 1
                j += 1
            elif nums[j+1] == 1:
                j += 1
            else:
                if nums[i] == 0:
                    num_zeroes += 1
                i += 1
            if (length := j - i + 1) > max_length:
                max_length = length
        return max_length

                