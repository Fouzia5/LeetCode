class Solution:
    def minBitwiseArray(self, nums):
        ans = []
        for n in nums:
            if n % 2 == 0:
                ans.append(-1)
            else:
                c = 0
                x = n
                while x & 1:
                    c += 1
                    x >>= 1
                ans.append(n - (1 << (c - 1)))
        return ans
