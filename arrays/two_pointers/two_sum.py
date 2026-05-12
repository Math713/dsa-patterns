from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> list[int] | None:
        hash_map = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in hash_map:
                return [hash_map[diff], i]

            hash_map[n] = i
        return None

print(Solution().two_sum([3,4,5,6], 7))