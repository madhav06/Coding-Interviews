# Given an array of integers A of size N and an integer B.

# array A is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).

# You are given a target value B to search. If found in the array, return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# NOTE:- Array A was sorted in non-decreasing order before rotation.

# Input 1:
#     A = [4, 5, 6, 7, 0, 1, 2, 3]
#     B = 4
# Output 1:
#     0
# Explanation 1:
#  Target 4 is found at index 0 in A.


# Input 2:
#     A = [5, 17, 100, 3]
#     B = 6
# Output 2:
#     -1

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if B == A[mid]:
                return mid
            elif A[mid] <= A[high]:
                if( B > A[mid]) & (B <= A[high]):
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (A[low] <= B) & (B < A[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
        return -1