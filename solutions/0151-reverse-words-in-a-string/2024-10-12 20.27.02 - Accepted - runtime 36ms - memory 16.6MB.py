class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([ss2 for ss in s.split(" ") if (ss2 := ss.replace(" ", ""))][::-1])