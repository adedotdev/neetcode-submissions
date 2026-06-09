class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        # 1. (DFS) Capture unsurrounded regions (O -> *)
        def mark(row, col):
            if row < 0 or row == ROWS or col < 0 or col == COLS or board[row][col] != "O":
                return
            board[row][col] = "*"
            mark(row+1, col) # top
            mark(row-1, col) # bottom
            mark(row, col+1) # right
            mark(row, col-1) # left

        for i in range(ROWS):
            mark(i, 0)      # first column
            mark(i, COLS-1) # last column

        for i in range(COLS):
            mark(0, i)      # first row
            mark(ROWS-1, i) # last row

        
        for i in range(ROWS):
            for j in range(COLS):
                # 2. Capture surrounded regions (O -> X)
                if board[i][j] == "O":
                    board[i][j] = "X"
                
                # 3. Uncapture unsurrounded regions (* -> O)
                if board[i][j] == "*":
                    board[i][j] = "O"
        