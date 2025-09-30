class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        def solve (nums,n):
            newnums= [0]*n
            if n==1:
                return nums[0]
            for i in range(n-1):
                newnums[i]=((nums[i]+nums[i+1])%10)
            return solve(newnums,n-1)
        return solve(nums,len(nums))

        