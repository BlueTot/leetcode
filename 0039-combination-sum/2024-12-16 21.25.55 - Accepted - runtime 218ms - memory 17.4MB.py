class Solution:

    def possibilities(self, candidates, target, selection=[]):
        if (s := sum(selection)) == target:
            return set([tuple(sorted(selection))])
        outputs = set()
        for num in candidates:
            if s + num <= target:
                output = self.possibilities(candidates, target, selection+[num])
                outputs |= output
        return outputs


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return [list(possibility) for possibility in self.possibilities(candidates, target)]