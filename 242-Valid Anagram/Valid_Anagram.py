class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        return countS == countT
"""
Example: s = "apple", t = "paple"

Count Characters in s = "apple"
Iteration 1 (i = 0):

s[i] = 'a'

countS.get('a', 0) → 0 (since 'a' is not yet in countS).

We update countS: countS['a'] = 0 + 1 = 1.

countS is now: {'a': 1}

Iteration 2 (i = 1):

s[i] = 'p'

countS.get('p', 0) → 0 (since 'p' is not yet in countS).

We update countS: countS['p'] = 0 + 1 = 1.

countS is now: {'a': 1, 'p': 1}

Iteration 3 (i = 2):

s[i] = 'p'

countS.get('p', 0) → 1 (since we already counted 'p' once before).

We update countS: countS['p'] = 1 + 1 = 2.

countS is now: {'a': 1, 'p': 2}

Iteration 4 (i = 3):

s[i] = 'l'

countS.get('l', 0) → 0 (since 'l' is not yet in countS).

We update countS: countS['l'] = 0 + 1 = 1.

countS is now: {'a': 1, 'p': 2, 'l': 1}

Iteration 5 (i = 4):

s[i] = 'e'

countS.get('e', 0) → 0 (since 'e' is not yet in countS).

We update countS: countS['e'] = 0 + 1 = 1.

countS is now: {'a': 1, 'p': 2, 'l': 1, 'e': 1}

At the end of the loop, countS looks like this:

python
Copy
Edit
countS = {'a': 1, 'p': 2, 'l': 1, 'e': 1}
Part 2: Count Characters in t = "paple"
Iteration 1 (i = 0):

t[i] = 'p'

countT.get('p', 0) → 0 (since 'p' is not yet in countT).

We update countT: countT['p'] = 0 + 1 = 1.

countT is now: {'p': 1}

Iteration 2 (i = 1):

t[i] = 'a'

countT.get('a', 0) → 0 (since 'a' is not yet in countT).

We update countT: countT['a'] = 0 + 1 = 1.

countT is now: {'p': 1, 'a': 1}

Iteration 3 (i = 2):

t[i] = 'p'

countT.get('p', 0) → 1 (since 'p' is already counted once).

We update countT: countT['p'] = 1 + 1 = 2.

countT is now: {'p': 2, 'a': 1}

Iteration 4 (i = 3):

t[i] = 'l'

countT.get('l', 0) → 0 (since 'l' is not yet in countT).

We update countT: countT['l'] = 0 + 1 = 1.

countT is now: {'p': 2, 'a': 1, 'l': 1}

Iteration 5 (i = 4):

t[i] = 'e'

countT.get('e', 0) → 0 (since 'e' is not yet in countT).

We update countT: countT['e'] = 0 + 1 = 1.

countT is now: {'p': 2, 'a': 1, 'l': 1, 'e': 1}
compare both and will get the answer.
countS = {'a': 1, 'p': 2, 'l': 1, 'e': 1}

countT = {'p': 2, 'a': 1, 'l': 1, 'e': 1}

other bruteforce method:

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t
""" 
        