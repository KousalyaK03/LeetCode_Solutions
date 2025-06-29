# Last updated: 6/29/2025, 3:48:43 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False
        s1_count = Counter(s1)
        window_count = Counter(s2[:len_s1])

        if window_count == s1_count:
            return True
        
        for i in range(len_s1, len_s2):
            start_char = s2[i-len_s1]
            new_char = s2[i]

            window_count[new_char] += 1
            window_count[start_char] -= 1

            if window_count[start_char] == 0:
                del window_count[start_char]

            if window_count == s1_count:
                return True
        return False