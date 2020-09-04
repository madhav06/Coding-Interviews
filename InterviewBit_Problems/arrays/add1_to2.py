# Given a non-negative number represented as an array of digits,

# add 1 to the number ( increment the number represented by the digits ).

# The digits are stored such that the most significant digit is at the head of the list.

# Example:

# If the vector has [1, 2, 3]

# the returned vector should be [1, 2, 4]

# as 123 + 1 = 124.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    
    def plusOne(self, A):
        # 
        n = len(A)
        if n < 1:
            return [1]
        for i in range(n-1, -1, -1):
            if A[i] == 9:
                A[i] = 0
            else:
                A[i] = A[i] + 1
                
            if A.count(0) == len(A):
                A[0] = 1
                A.append(0)