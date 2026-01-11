class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
        valid = set(bank)
        queue = deque([(startGene, 0)])

        def neighbours(gene):
            for i in range(len(gene)):
                for char in ('A', 'C', 'G', 'T'):
                    if gene[i] != char:
                        yield gene[:i] + char + gene[i+1:]
        
        visited = set()
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for mutation in neighbours(gene):
                if mutation not in visited and mutation in valid:
                    visited.add(mutation)
                    queue.append((mutation, steps + 1))
        
        return -1