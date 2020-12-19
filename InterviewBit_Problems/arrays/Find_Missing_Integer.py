# python3

# Given an unsorted integer array, find the first missing positive integer.

# Example:

# Given [1,2,0] return 3,

# [3,4,-1,1] return 2,

# [-8, -7, -6] returns 1

# Your algorithm should run in O(n) time and use constant space.



class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        positive = {}
        initialPosition = 1
        for n in A:
            if n>0:
                positive[n]=1
        while positive.get(initialPosition,0):
            initialPosition += 1
        
        return initialPosition

