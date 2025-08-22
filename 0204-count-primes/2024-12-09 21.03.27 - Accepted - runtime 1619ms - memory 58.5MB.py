class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True]*n
        for i in range(2, int(n**0.5)+1):
            if isPrime[i]:
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return sum([1 for i in range(2, n) if isPrime[i]])