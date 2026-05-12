# Products of Array Except Self

# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n

        for i in range(n):
            prod=1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]
            res[i] = prod
        return res                      

    