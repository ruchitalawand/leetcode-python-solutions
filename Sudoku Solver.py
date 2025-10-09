Sudoku Solver 

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(r, c, ch):
            # Check row
            for i in range(9):
                if board[r][i] == ch:
                    return False
            # Check column
            for i in range(9):
                if board[i][c] == ch:
                    return False
            # Check 3x3 box
            start_row, start_col = 3 * (r // 3), 3 * (c // 3)
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for ch in '123456789':
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        solve()
