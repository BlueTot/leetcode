class Solution:
    def isPalindrome(self, x: int) -> bool:
        lst = [i for i in str(x)]
        lst.reverse()
        s = "".join(lst)
        return str(x) == s