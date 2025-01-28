#User function Template for python3
from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Code here
        ans = set(permutations(s))
        return sorted([''.join(p) for p in ans])