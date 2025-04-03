# Last updated: 4/2/2025, 5:35:58 PM
'''
Brute Force approach:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
'''
#  Optimised approach:

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen_numbers = set()  # to store unique numbers we use set()

        for number in nums:  # to loop through each number in the list
            if number in seen_numbers:   # if the number is already seen in the list 
                return True  # then return true
            seen_numbers.add(number)   # if its a new number, add the number to the list
        return False  # if there are no duplicates return false

'''
Example:1
seen numbers = set()
for 1 in the number list
    if 1 in seen? no, false.
     seen_numbers.add(1)

seen_numbers = set(1)
--------------
seen_numbers = set(1)
for 2 in number list
    if 2 in seen? no, false.
    seen_numbers.add(2)
seen_numbers = set(1,2)
--------------
seen_numbers = set(1,2)
for 3 in number list
    if 3 in seen? no, false.
    seen_numbers.add(3)
seen_numbers = set(1,2,3)

--------------
seen_numbers = set(1,2,3)
for 1 in number list
    if 1 in seen? yes, true.
     seen_numbers.add()  # duplicates
seen_numbers = set(1,2,3)


i = 0 = 1
j = (0+1) = 1 = 2
nums[i] = 1
nums[j] = 2
if false 1 == 2


i = 0 = 1
j = (1+1) = 2 = 3

nums[i] = 1
nums[j] = 3
if false 1 == 3


i = 0 = 1
j = (0+1) = 1 = 2
nums[i] = 1
nums[j] = 1
if true 1 == 1

'''