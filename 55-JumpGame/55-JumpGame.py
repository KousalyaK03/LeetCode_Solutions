# Last updated: 7/8/2025, 2:45:27 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas = gas - 1
        return True
