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
       
        if A == [0]:
            return [1]
        l = A[::-1] # reverse the list and store
        
        l += [0] # increase size by 1
        x = 1
        for i in range(len(l)):
            l[i] += x
            x = l[i] // 10
            l[i] = l[i] % 10
        l = l[::-1]
        for i in range(len(l)):
            if l[i] != 0:
                x = i
                break
        return l[i:]
            
