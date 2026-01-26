class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        res = []
        min_diff = float('inf')
        for i in range(1, len(arr)):
            d = arr[i] - arr[i - 1]
            if d < min_diff:
                min_diff = d
                res = [[arr[i - 1], arr[i]]]
            elif d == min_diff:
                res.append([arr[i - 1], arr[i]])
        return res

        