class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = {}
        for equation, value in zip(equations, values):
            start, end = equation
            if start not in graph: graph[start] = {}
            graph[start][end] = value
            if end not in graph: graph[end] = {}
            graph[end][start] = 1/value
        
        def calculate(start: str, end: str, visited) -> float:
            if start in visited or start not in graph:
                return -1
            if start == end:
                return 1
            visited.add(start)
            for neighbour, weight in graph[start].items():
                score = calculate(neighbour, end, visited)
                if score != -1:
                    return graph[start][neighbour] * score
            return -1
        
        output = []
        for start, end in queries:
            output.append(calculate(start, end, set()))
        return output
