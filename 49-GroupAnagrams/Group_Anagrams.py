class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        grouped = [False] * len(strs)

        for i in range(len(strs)):
            if grouped[i]:
                continue

            group = [strs[i]]
            grouped[i] = True

            for j in range(i+1, len(strs)):
                if not grouped[j] and sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    grouped[j] = True
            result.append(group)

        return result

""" 
grouped = [False, False, False, False, False, False]

result = []

i = 0, strs[0] = "act"

Not grouped → Start new group: group = ["act"]

Mark grouped[0] = True

Loop j = 1 to 5:

j=1: "pots" → sorted("act") ≠ sorted("pots") → skip

j=2: "tops" → sorted("act") ≠ sorted("tops") → skip

j=3: "cat" → same sorted → add to group, mark grouped[3] = True

j=4: "stop" → no match

j=5: "hat" → no match

Group: ["act", "cat"] → add to result
Now:

grouped = [True, False, False, True, False, False]
result = [["act", "cat"]]
i = 1, "pots"

Not grouped → start group = ["pots"], grouped[1] = True

Loop j = 2 to 5:

j=2: "tops" → match → add

j=3: already grouped

j=4: "stop" →  match → add

j=5: no match

Group: ["pots", "tops", "stop"]
Update:

grouped = [True, True, True, True, True, False]
result = [["act", "cat"], ["pots", "tops", "stop"]]
i = 2, 3, 4 → all grouped → skip

i = 5, "hat" → not grouped → group = ["hat"], mark grouped[5] = True
No other matches → group remains ["hat"]



optimised:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for word in strs:
            # Sort the word to use as key
            sorted_word = ''.join(sorted(word))
            # Add the word to the corresponding group
            anagram_groups[sorted_word].append(word)

        # Return all the groups
        return list(anagram_groups.values())
"""