from itertools import product

class Solution:

    def matrix_num(self, row, col):
        return 3 * (row // 3) + col // 3

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        N = 9
        cols = ([("row col", row_col) for row_col in
                 product(range(N), range(N))] +  
                [("row num", row_num) for row_num in
                 product(range(N), range(1, N + 1))] +  
                [("col num", col_num) for col_num in
                 product(range(N), range(1, N + 1))] +  
                [("matrix num", matrix_num) for matrix_num in product(range(N), range(1, N + 1))])

        rows = {}  # Initialise rows dictionary
        for row, col, num in product(range(N), range(N), range(1, N + 1)):
            # Populate rows dictionary with the columns that they match
            matrix_num = self.matrix_num(row, col)
            rows[(row, col, num)] = [("row col", (row, col)),
                                     ("row num", (row, num)),
                                     ("col num", (col, num)),
                                     ("matrix num", (matrix_num, num))]

        cols, rows = self.convert_to_sets(cols, rows)  # Convert cols into dictionary of sets for easy access from cols to rows

        for rowidx, row in enumerate(board):  # Iterate through all squares of the given board
            for colidx, sq in enumerate(row):
                if board[rowidx][colidx] != ".":  # If the number at the square is not 0
                    self.cover(cols, rows, (rowidx, colidx, int(board[rowidx][colidx])))

        for solution_set in self.solve(cols, rows):  # Iterate through all solutions of the board using DLX Solver
            for (row, col, num) in solution_set:  # Iterate through all squares
                board[row][col] = str(num)

    def convert_to_sets(self, cols, rows):  # Function to convert set to dictionary of sets for fast access
        cols = {col: set() for col in cols}  # Setup dictionary
        for row_id, row_contents in rows.items():  # Loop through rows
            for col in row_contents:  # Loop through cols
                cols[col].add(row_id)  # Add row to set
        return cols, rows  # Return dictionaries

    def solve(self, cols, rows, solution_set=[]):  # Dancing Links X main solver algorithm
        if not cols:  # Check if no more columns left in the matrix (base case)
            return [list(solution_set)]  # Return the solution set
        else:
            min_col = min(cols, key=lambda col: len(
                cols[col]))  # Get column with least number of intersecting rows (S-heuristic)
            sols = []  # Initialise list of solution sets
            for selected_row in list(cols[min_col]):  # Iterate thorugh rows, selecting a row to cover every time
                solution_set.append(selected_row)  # Add to solution set
                cols, cells_to_restore = self.cover(cols, rows, selected_row)  # Cover selected row and intersecting cols
                for sol in self.solve(cols, rows, solution_set):  # Recursively solve the reduced matrix
                    sols.extend([sol])  # Add solution set to list of solution sets
                cols = self.uncover(cols, cells_to_restore)  # Uncover
                solution_set.pop()  # Remove from solution set
            return sols  # return list of solution sets

    def cover(self, cols, rows, selected_row):  # Cover function
        cells_to_restore = set()  # Initialise set of cells to restore for uncover function
        cols_to_remove = set()  # Initialise set of cols to remove
        for col_to_remove in rows[selected_row]:  # Iterate through cols to remove
            cols_to_remove.add(col_to_remove)  # Add col to set of cols to remove
            for row_to_remove in cols[col_to_remove]:  # Iterate through rows to remove
                for intersecting_col in rows[row_to_remove]:  # Iterate through intersecting column of the row
                    cells_to_restore.add((intersecting_col, row_to_remove))  # Add cell to set of cells to restore
        for col, row in cells_to_restore:  # Loop through cells to restore
            cols[col].remove(row)  # Remove the cell from the matrix
        for col in cols_to_remove:  # Loop through cols to remove
            cols.pop(col)  # Remove the col
        return cols, cells_to_restore  # Return the new cols dictionary and cells to restore (rows dictionary untouched, only connections removed)

    def uncover(self, cols, cells_to_restore):  # Uncover function
        for col, row in cells_to_restore:  # Loop through cells to restore
            if col not in cols:  # If col has been removed
                cols[col] = set()  # Restore the set
            cols[col].add(row)  # Now add the row back to the set
        return cols  # Return the restored cols dictionary
