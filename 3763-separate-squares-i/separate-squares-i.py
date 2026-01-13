class Solution:
    def separateSquares(self, squares):
        total = 0.0
        for x, y, l in squares:
            total += l * l
        half = total / 2.0
        low = 0.0
        high = 1e10
        for _ in range(60):
            mid = (low + high) / 2.0
            below = 0.0
            for x, y, l in squares:
                if mid <= y:
                    continue
                if mid >= y + l:
                    below += l * l
                else:
                    below += (mid - y) * l
            if below < half:
                low = mid
            else:
                high = mid
        return low

        