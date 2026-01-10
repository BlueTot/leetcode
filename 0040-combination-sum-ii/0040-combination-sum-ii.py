class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()
        def populate(i: int, curr: list[int], curr_sum: int) -> None:
            if curr_sum >= target:
                if curr_sum == target:
                    res.add(tuple(sorted(curr[:])))
                return
            seen = set()
            for j in range(i, len(candidates)):
                if candidates[j] in seen:
                    continue
                curr.append(candidates[j])
                populate(j+1, curr, curr_sum + candidates[j])
                curr.pop()
                seen.add(candidates[j])

        populate(0, [], 0)
        return [list(t) for t in res]