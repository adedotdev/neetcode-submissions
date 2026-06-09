class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_of_islands = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(matrix, row, col):
            if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
                return
            if matrix[row][col] == "0":
                return

            matrix[row][col] = "0"

            dfs(matrix, row+1, col) # top
            dfs(matrix, row-1, col) # bottom
            dfs(matrix, row, col+1) # right
            dfs(matrix, row, col-1) # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    num_of_islands += 1
        
        return num_of_islands


    


        