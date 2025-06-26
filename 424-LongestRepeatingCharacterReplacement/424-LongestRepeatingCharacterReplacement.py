# Last updated: 6/26/2025, 4:56:49 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_count = 0
        max_len = 0

        for right in range(len(s)):
            index = ord(s[right]) - ord('A')
            count[index] += 1
            max_count = max(max_count, count[index])

            window_len = right - left + 1
            changes = window_len - max_count

            if changes > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)

        return max_len
