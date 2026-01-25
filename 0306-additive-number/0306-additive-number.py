class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        def backtrack(i, k, num1, num2):
            if i >= len(num) and k >= 3:
                return True
            if k == 0:
                for j in range(i, len(num)):
                    if num[i] != '0' and backtrack(j+1, k + 1, 0, int(num[i:j+1])):
                        return True
                return False
            elif k == 1:
                for j in range(i, len(num)):
                    if num[i] != '0' and backtrack(j+1, k + 1, num2, int(num[i:j+1])):
                        return True
                return False
            else:
                for j in range(i, len(num)):
                    if (s := int(num[i:j+1])) == num1 + num2 and num[i] != '0':
                        if backtrack(j+1, k+1, num2, s):
                            return True
                return False
        
        return backtrack(0, 0, 0, 0)

        