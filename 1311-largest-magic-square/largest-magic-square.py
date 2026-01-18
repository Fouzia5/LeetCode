class Solution:
    def largestMagicSquare(self, grid):
        m = len(grid)
        n = len(grid[0])

        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*n for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]

        ans = 1

        for k in range(2, min(m, n) + 1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    s = row[i][j+k] - row[i][j]
                    ok = True

                    for r in range(i, i+k):
                        if row[r][j+k] - row[r][j] != s:
                            ok = False
                            break

                    for c in range(j, j+k):
                        if col[i+k][c] - col[i][c] != s:
                            ok = False
                            break

                    d1 = 0
                    d2 = 0
                    for t in range(k):
                        d1 += grid[i+t][j+t]
                        d2 += grid[i+t][j+k-1-t]

                    if d1 != s or d2 != s:
                        ok = False

                    if ok:
                        ans = k

        return ans
