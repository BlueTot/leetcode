class Solution:
    def candy(self, ratings: List[int]) -> int:

        candiesL = [1]* len(ratings)
        candiesR = [1]* len(ratings)
        
        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i-1]:
                candiesL[i] = candiesL[i-1] + 1
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candiesR[i] = candiesR[i+1]+1

        print(candiesL, candiesR)

        return sum([max(i, j) for i, j in zip(candiesL, candiesR)])

        return sum(candies)