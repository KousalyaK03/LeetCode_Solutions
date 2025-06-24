# Last updated: 6/23/2025, 9:42:39 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        for i in range(len(strs[0])):
            if i >= len(strs[-1]) or strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]


"""
Bruteforce:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs[1:]:
                if i>= len(word) or word[i] != char:
                    return strs[0][:i]
        return strs[0]

More optimised one(Horizontal scanning):
if not strs:
    return ""

strs.sort()  # Sort the array

for i in range(len(strs[0])):
    if i >= len(strs[-1]) or strs[0][i] != strs[-1][i]:
        return strs[0][:i]

return strs[0]

"""