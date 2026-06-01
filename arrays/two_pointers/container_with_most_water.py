from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            b = right - left
            h = min(height[left], height[right])

            current_area = b * h

            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))