class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i, char in enumerate(s) if char in "aeiouAEIOU"]
        s = list(s)
        for index, i in enumerate(vowels[:len(vowels)//2]):
            s[i], s[vowels[-(index+1)]] = s[vowels[-(index+1)]], s[i]
        return "".join(s)