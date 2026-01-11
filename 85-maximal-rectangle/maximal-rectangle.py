class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix : return 0
        row, cols = len(matrix), len(matrix[0])

        hights = [0] * (cols + 1)
        max_area = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    hights[i] += 1

                else:
                    hights[i] = 0

            stack = [-1]
            for i in range(cols + 1):
                while stack[-1] != -1 and hights[stack[-1]] >= hights[i]:
                    h = hights[stack.pop()]
                    w = i - stack[-1] -1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
        