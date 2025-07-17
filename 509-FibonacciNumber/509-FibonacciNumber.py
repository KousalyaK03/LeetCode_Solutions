# Last updated: 7/17/2025, 2:55:14 PM
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        prev1, prev2 = 1, 0
        for _ in range(2, n + 1):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr

        return prev1