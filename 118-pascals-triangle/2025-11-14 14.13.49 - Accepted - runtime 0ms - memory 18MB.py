class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        if numRows == 1:
            return [[1]]
        rows = [[1], [1,1]]
        for _ in range(numRows-2):
            curr = [1]
            for i in range(len(rows[-1])-1):
                curr.append(rows[-1][i] + rows[-1][i+1])
            curr.append(1)
            rows.append(curr)
        return rows
        