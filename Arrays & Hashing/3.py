# Two Sum

# Input: 
# nums = [3,4,5,6], target = 7
# Output: [0,1]

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in D:
                return [D[complement],i]
            D[num] = i
        return []


  