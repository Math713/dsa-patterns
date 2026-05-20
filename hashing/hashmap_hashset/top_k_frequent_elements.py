from collections import defaultdict
from typing import List

class Solution:
    """
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]: Lambda method
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        return sorted(sorted_elements[:k])
    """

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]: # Bucket Sort method
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num,freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket) -1,0,-1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res

print(Solution().top_k_frequent([1,2,2,3,3,3], 2))

