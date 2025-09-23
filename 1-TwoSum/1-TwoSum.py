# Last updated: 9/23/2025, 1:01:03 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_index = {}

        for i, num in enumerate((nums)):
            complement = target -  num

            if complement in num_index:
                return [num_index[complement], i]
            num_index[num] = i
        

        '''
        num_index = {}
        for i, num in enumerate((nums)):
            complement = target - num
            if complement in num_index:
                return [num_index[complement], i]
            num_index[num] = i

     
        for i in range(len(nums)):
            for j in range(i + 1, len(nums))

        n = len(nums)
        for i in range(n): - O(n).          # O(n) * O(n) = O(n^2) + O(1)
            for j in range(i + 1, n): - O(n)
                if nums[i] + nums[j] == target: - O(1)
                    return [i, j] - O(1)


        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        for i in range (len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} - {2:0, 7:1, 11:2, 15:3}
        n = len(nums)

        # Build the hash table
        for i in range(n): i = 0 to 3
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n): # i = 0
            complement = target - nums[i]  = 9 - 2 = 7
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []  # No solution found


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