# Car Fleet

# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.
# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
