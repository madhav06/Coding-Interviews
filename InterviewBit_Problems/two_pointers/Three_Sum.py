# Python 3 Code

'''
Given an array S, of n integers, find three integers in S such that the sum is closest to a given number,target.
Return the sum of the three integers.

Example:

S = {-1, 2, 1, -4}
and target = 1

the sum that is c;osest to target is 2 (-1 + 2 + 1 = 2)
'''

class Solution:
    # @param A: list of ints
    # @param B: int
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort()
        n = len(A)
        result = float('inf')

        for i in range(0, n-2):
            left = i + 1
            right = n - 1

            while left < right:
                s = A[i] + A[left] + A[right]

                if abs(result - B) > abs(s - B):
                    result = s
                if s == B:
                    return B
                if s > B:
                    right -= 1

                else:
                    left += 1
        return result
