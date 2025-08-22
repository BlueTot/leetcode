class Solution:
    def romanToInt(self, s: str) -> int:
        idx = 0
        total = 0
        values = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900,
                    "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while idx < len(s):
            if idx < len(s)-1 and (chars := s[idx:idx+2]) in ("IV", "IX", "XL", "XC", "CD", "CM"):
                idx += 2
                total += values[chars]
            else:
                total += values[s[idx]]
                idx += 1
        return total
                    
        