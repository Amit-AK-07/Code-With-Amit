#User function Template for python3

class Solution:
    def numIslands(self, grid):
        # code here
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L':
                    self.dfs(grid, i, j, n, m)
                    count += 1
        return count
    
    def dfs(self, grid, i, j, n, m):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 'L':
            return
        grid[i][j] = 'V'  # Mark as visited
        # Check all 8 directions
        self.dfs(grid, i+1, j, n, m)
        self.dfs(grid, i-1, j, n, m)
        self.dfs(grid, i, j+1, n, m)
        self.dfs(grid, i, j-1, n, m)
        self.dfs(grid, i+1, j+1, n, m)
        self.dfs(grid, i+1, j-1, n, m)
        self.dfs(grid, i-1, j+1, n, m)
        self.dfs(grid, i-1, j-1, n, m)

