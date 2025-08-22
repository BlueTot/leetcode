class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combos = []
        def populate(i, k, curr=[]):
            if k == 0:
                combos.append(curr)
            for j in range(i, n+1):
                populate(j+1, k-1, curr + [j])
        
        populate(1, k)
        return combos