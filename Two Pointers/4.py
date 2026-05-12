# Container With Most Water

# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36
from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res