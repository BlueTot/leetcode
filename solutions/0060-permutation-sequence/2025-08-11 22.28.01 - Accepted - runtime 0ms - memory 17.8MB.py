from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        curr = ""
        while n > 0:
            
            # calculate first digit by subtracting number of ways
            # to arrange remaining digits
            amount = 0
            fac = factorial(n-1)
            while k > fac:
                k -= fac
                amount += 1

            # add to curr, and remove that digit
            curr += str(nums[amount])
            nums.pop(amount)
            n -= 1

        return curr
