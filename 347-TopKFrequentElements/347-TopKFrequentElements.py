# Last updated: 6/25/2025, 5:55:01 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
            

"""
        num_index = {}
        for i, num in enumerate((numbers)):
            complement = target - num
            if complement in num_index:
                return [num_index[complement] + 1, i + 1]
            num_index[num] = i
"""