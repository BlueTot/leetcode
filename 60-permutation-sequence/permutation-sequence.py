from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        curr = ""
        while n > 0:
            
            amount = 0
            fac = factorial(n-1)
            while k > fac:
                k -= fac
                amount += 1

            curr += str(nums[amount])
            nums.pop(amount)
            n -= 1

        return curr
        # 3! = 6. 9 // 6 = 1, so we use second position - 2
        # 9 - 6 = 3 [1,3,4]
        # 2! = 2. 3 // 2 = 1, so we use second position - 3
        # 3 - 2 = 1 [1,4]
        # 1! = 1. 1 // 1 = 1
