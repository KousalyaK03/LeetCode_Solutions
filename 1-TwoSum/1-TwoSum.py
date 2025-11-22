# Last updated: 11/21/2025, 5:40:15 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, value in enumerate(nums):
            needed = target - value

            if needed in seen:
                return [seen[needed], index]
            seen[value] = index
            