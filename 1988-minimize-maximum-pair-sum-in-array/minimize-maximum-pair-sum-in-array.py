class Solution:
    def minPairSum(self, nums):
        nums.sort()
        i,j=0,len(nums)-1
        ans=0
        while i<j:
            ans=max(ans,nums[i]+nums[j])
            i+=1
            j-=1
        return ans
