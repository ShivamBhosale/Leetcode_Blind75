class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(i,dp):
            if i==0:
                return 1
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]

            dp[i]= fib(i-1,dp) + fib(i-2,dp)

            return dp[i]
        dp=[-1]*(n+1) 
        return fib(n,dp)
