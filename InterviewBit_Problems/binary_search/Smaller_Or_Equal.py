# Problem Description

# Given an sorted array A of size N. Find number of elements which are less than or equal to B.

# NOTE: Expected Time Complexity O(log N)



# Problem Constraints
# 1 <= N <= 106

# 1 <= A[i], B <= 109



# Input Format
# First agument is an integer array A of size N.

# Second argument is an integer B.



# Output Format
# Return an integer denoting the number of elements which are less than or equal to B.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        start = 0
        end = len(A)-1
 
        while start<=end:
            mid = (start+end)//2
            if A[mid]<=B:
                start = mid+1
            else:
                end = mid-1
        return start