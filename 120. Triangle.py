class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def helper(triangle ,row ,ind):
            if row == len(triangle):
                return 0
            return triangle[row][ind] + min(helper(triangle , row+1,ind), helper(triangle,row+1,ind+1))

        # return helper(triangle,0,0)
        dp = [0] * (len(triangle)+1)
        for row in triangle[::-1]:
            for i,n in enumerate(row):
                dp[i] = n+ min(dp[i],dp[i+1])
        return dp[0]


        