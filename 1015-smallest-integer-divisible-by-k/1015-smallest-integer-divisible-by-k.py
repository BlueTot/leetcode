class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        curr = 1
        total = 0
        count = 0

        seen = set()

        while (count == 0 or total != 0):
            
            seen.add(total)
            total = (total + curr) % k
            curr = (curr * 10) % k

            if total != 0 and total in seen:
                return -1
            
            count += 1
        
        return count