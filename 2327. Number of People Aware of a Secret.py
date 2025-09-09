class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0]*(n)
        dp[0]=1
        mod = 10**9 + 7
        peoplesharing=0
        for i in range(delay,n):
            peoplesharing+= dp[i-delay]
            dp[i] = peoplesharing
            if i-forget+1>=0:
                peoplesharing-=dp[i-forget+1]
           

        return sum(dp[-forget:]) % mod
        
        