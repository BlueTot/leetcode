class Solution:
    def isAdditiveNumber(self, num: str) -> bool:

        # we do backtracking by selecting the next number to put into the list
        # we keep track of the past two sums to calculate the next sum

        # condition num[i] != '0' or j == i is to make sure we don't have numbers 
        # with more than 1 digit starting with 0

        # if we reach the end, then there is a match

        # i: starting position.
        # k: the number of terms
        # num1, num2: are previous sums.
        
        def backtrack(i, k, num1, num2):
            if i >= len(num) and k >= 3:
                return True
            if k == 0:
                for j in range(i, len(num)):
                    if num[i] != '0' or j == i:
                        if backtrack(j+1, k + 1, 0, int(num[i:j+1])):
                            return True
                return False
            elif k == 1:
                for j in range(i, len(num)):
                    if num[i] != '0' or j == i:
                        if backtrack(j+1, k + 1, num2, int(num[i:j+1])):
                            return True
                return False
            else:
                for j in range(i, len(num)):
                    if (s := int(num[i:j+1])) == num1 + num2 and (num[i] != '0' or j == i):
                        if backtrack(j+1, k+1, num2, s):
                            return True
                return False
        
        return backtrack(0, 0, 0, 0)

        