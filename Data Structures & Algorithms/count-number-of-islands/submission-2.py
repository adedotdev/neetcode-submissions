class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        num_of_islands = 0
        
        def dfs(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            dfs(r+1, c) # top
            dfs(r-1, c) # bottom
            dfs(r, c+1) # right
            dfs(r, c-1) # left

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_of_islands += 1
        
        return num_of_islands


    


        