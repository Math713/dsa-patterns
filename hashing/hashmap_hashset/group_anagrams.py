from typing import List
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            ans[key].append(s)

        return list(ans.values())

print(Solution().group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]))