# Last updated: 7/8/2025, 2:56:39 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        # will start from index 0 => n = 2
        for n in nums:
            if gas < 0:  # this means we have no steps to jump ahead so False
                return False
            elif n > gas:  # if number is > 0 then we can intialise it to gas so refuel it
                gas = n
            gas = gas - 1  # we can decrement the fuel by 1 because we should move forward
        return True
# repeat til all elements are done and if the gas < 0 until end, we can print True
