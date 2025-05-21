class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Step 1: Filter all elements not equal to val into a new list
        result = [num for num in nums if num != val]

        # Step 2: Overwrite original nums with result values
        for i in range(len(result)):
            nums[i] = result[i]

        # Step 3: Return the count of valid elements
        return len(result)


"""
Initial nums = [3, 2, 2, 3]

We build result = [num for num in nums if num != val]

num = 3 → equals val → skip

num = 2 → not val → include

num = 2 → not val → include

num = 3 → equals val → skip
➤ result = [2, 2]

Overwrite original nums using this filtered result:

i = 0 → nums[0] = result[0] = 2

i = 1 → nums[1] = result[1] = 2
➤ nums = [2, 2, 2, 3] (but only first two values matter)

Return: len(result) = 2


Optimised approach:
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to place the next valid element
        k = 0

        # Loop through each element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Place current element at index k
                k += 1             # Move k forward for next valid element

        return k  # Number of valid elements

"""