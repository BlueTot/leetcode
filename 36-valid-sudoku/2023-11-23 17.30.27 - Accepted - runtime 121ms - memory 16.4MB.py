class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            for num in range(1, 10):
                if row.count(str(num)) > 1:
                    return False
        
        cols = ([board[row][col] for row in range(9)] for col in range(9))

        for col in cols:
            for num in range(1, 10):
                if col.count(str(num)) > 1:
                    return False
        
        boxes = [[] for _ in range(9)]
        for row in range(9):
            for col in range(9):
                box_num = 3 * (row // 3) + col // 3
                boxes[box_num].append(board[row][col])
        
        for box in boxes:
            for num in range(1, 10):
                if box.count(str(num)) > 1:
                    return False
        
        return True

        