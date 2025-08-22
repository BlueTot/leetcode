class Solution:

    def traverse(self, digits, graph):
        if digits == "":
            return [""]
        combs = []
        for letter in graph[int(digits[0])]:
            for continuation in self.traverse(digits[1:], graph):
                combs.append(letter+continuation)
        return combs
        

    def letterCombinations(self, digits: str) -> List[str]:
        graph = {1: [], 2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"], 
        5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 8: ["t", "u", "v"],
        9: ["w", "x", "y", "z"]}
        return [] if (output := self.traverse(digits, graph)) == [""] else output
        