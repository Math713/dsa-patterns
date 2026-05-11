from typing import List

class Solution:
    def has_duplicate(self, nums:List[int]) -> bool:
        return len(set(nums)) < len(nums)

print(Solution().has_duplicate([1,2,3,2]))