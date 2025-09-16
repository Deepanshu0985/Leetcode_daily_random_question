class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        top = 0 
        for x in nums:
            while top>0 and gcd(nums[top-1],x)>1:
                x = lcm(nums[top-1],x)
                top-=1
            nums[top] = x
            top+=1
        return nums[:top]
