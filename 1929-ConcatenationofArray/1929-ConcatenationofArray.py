# Last updated: 4/19/2025, 5:34:46 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums + nums
        return ans
"""
Optimised Approach:
 n = len(nums)
        result = [0] * (2 * n)  # Preallocate list of size 2n
        for i in range(n):
            result[i] = nums[i]
            result[i + n] = nums[i]
        return result
"""