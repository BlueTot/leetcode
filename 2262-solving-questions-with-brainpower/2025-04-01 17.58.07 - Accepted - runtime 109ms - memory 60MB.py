class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        array = {i : 0 for i in range(len(questions))}
        for i in range(len(array)-1, -1, -1):
            array[i] = max(array.get(i+1, 0), questions[i][0] + array.get(i+questions[i][1]+1, 0))
        return max(array.values())