# Last updated: 4/23/2025, 6:05:38 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i






'''
        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j


Input: nums = [2,3,7,10]
Output: [0,1]

Input: nums = [11, 13, 19, 20]
Output: [2,3]
i = 0 = 2
j = (1+0) = 3
nums[i] = 2
nums[j] = 3
if something == something_else
2,3,7,10
(2 + 1 ) == 3

2  == 3 - 1
    
    
    
    
    -----
i = 0 = 3
j = (1+1) = 2 = 4
target = 6
nums[i] = 3
nums[j] = 4
if false 6 == 3 + 4

--------

i = 1 = 2
j = (1+1) = 2 = 4
target = 6
nums[i] = 3
nums[j] = 4
if true 6 == 2 + 4
return 1,2
'''