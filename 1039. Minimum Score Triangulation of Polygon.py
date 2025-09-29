class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def helper(values, i, j,dp):
            if i + 1 == j:
                return 0
            if dp[i][j]:
                return dp[i][j]
            ans = float('inf')
            for k in range(i + 1, j):
                ans = min(ans, values[i] * values[j] * values[k] +helper(values, i, k,dp) + helper(values, k, j,dp))
            dp[i][j] = ans
            return dp[i][j]

        n= len(values)
        dp = [[0]*n for _ in range(n)]

        return helper(values, 0, len(values) - 1,dp)
