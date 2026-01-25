class Solution:
    def minimumDifference(self, nums, k):
        if k == 1:
            return 0
        nums.sort()
        m = float('inf')
        for i in range(len(nums) - k + 1):
            m = min(m, nums[i + k - 1] - nums[i])
        return m
