from typing import List
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        row_sum = [0] * m
        col_sum = [0] * n
        total = 0
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
                row_sum[i] += grid[i][j]
                col_sum[j] += grid[i][j]
        if total % 2 != 0:
            return False
        upper = 0
        for i in range(m - 1):
            upper += row_sum[i]
            if upper == total - upper:
                return True
        left = 0
        for j in range(n - 1):
            left += col_sum[j]
            if left == total - left:
                return True
        return False