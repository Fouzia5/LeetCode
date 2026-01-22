class Solution:
    def minimumPairRemoval(self, nums):
        ans = 0
        while True:
            ok = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    ok = False
                    break
            if ok:
                return ans
            mn = nums[0] + nums[1]
            idx = 0
            for i in range(1, len(nums)-1):
                if nums[i] + nums[i+1] < mn:
                    mn = nums[i] + nums[i+1]
                    idx = i
            nums[idx] = nums[idx] + nums[idx+1]
            nums.pop(idx+1)
            ans += 1
