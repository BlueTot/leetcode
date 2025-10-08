class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            if (key := "".join(sorted(s))) not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)
        return list(groups.values())