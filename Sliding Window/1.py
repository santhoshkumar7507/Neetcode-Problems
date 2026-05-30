# Best Time to Buy and Sell Stock

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                result = max(result,sell-buy)
        return result
