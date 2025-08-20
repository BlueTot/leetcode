class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        result = []
        def populate(curr, length, curr_elems=[], curr_sum = 0):
            if length == k:
                if curr_sum == n:
                    result.append(curr_elems[:])
                return
            if curr_sum > n: return
            for i in range(curr, 10):
                curr_elems.append(i)
                populate(i+1, length+1, curr_elems, curr_sum + i)
                curr_elems.pop()
        
        populate(1, 0)
        return result
