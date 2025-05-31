# Last updated: 5/30/2025, 5:56:26 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
           
"""          
            result = [num for num in nums if num != val]

            for i in range(len(result)):
                nums[i] = result[i]

            return len(result)
"""