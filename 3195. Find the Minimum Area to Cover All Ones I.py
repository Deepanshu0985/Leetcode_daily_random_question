class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        minrow, maxrow = n, -1
        mincol, maxcol = m, -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    minrow = min(minrow, i)
                    maxrow = max(maxrow, i)
                    mincol = min(mincol, j)
                    maxcol = max(maxcol, j)

        if maxrow == -1:
            return 0

        return (maxrow - minrow + 1) * (maxcol - mincol + 1)
