
# Python3


# Given an integar A.

# Compute and return the square root of A.

# If A is not a perfect square, return floor(sqrt(A)).

# DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY

import math

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        return math.floor(math.sqrt(A))


# Python 2.7

class Solution:
  # @param A : integer
  # @return an integer
  def sqrt(self, A):
    left = 0
    right = A
    while left <= right:
      mid = (left + right) // 2
      if mid * mid <= A:
        left = mid + 1
      else:
        right = mid - 1
    return right


