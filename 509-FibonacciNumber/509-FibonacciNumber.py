# Last updated: 7/17/2025, 3:13:34 PM
class Solution:
    def fib(self, n: int, memo = {}) -> int:

        if n <= 1:
            return n
        prev1, prev2 = 1, 0
        for _ in range(2, n + 1):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr

        return prev1

"""
Tabulation (Bottom Up approach):
TC: O(n) SC: O(n) 

        if n <= 1:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

Memoization (Top Down approach):
TC: O(n) SC: O(n)
        if memo is None:
            memo = {}

        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        return memo[n]

"""

        