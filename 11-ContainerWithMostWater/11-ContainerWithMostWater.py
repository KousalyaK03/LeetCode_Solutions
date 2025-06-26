# Last updated: 6/26/2025, 2:32:24 PM
# Approach:
# Use a two-pointer technique, initializing one pointer at the beginning and the other at the end of the array.
# Calculate the area formed between the two lines, then move the pointer pointing to the shorter line inward, as this maximizes the potential for a higher area.
# Continue until the pointers meet, keeping track of the maximum area found during the traversal.

# Time Complexity: O(n), where n is the number of elements in height
# Space Complexity: O(1), as we only use a constant amount of extra space
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

'''
        left, right = 0, len(height) - 1  # Initialize two pointers at both ends of the array
        max_area = 0  # Variable to store the maximum area found

        while left < right:
            # Calculate the area with the current pair of lines
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)  # Update max_area if the current area is greater

            # Move the pointer pointing to the shorter line inward to potentially find a larger area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area  # Return the maximum area found
'''