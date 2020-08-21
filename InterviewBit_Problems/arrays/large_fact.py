# Python3

# Problem Description
# Given a number A. Find the fatorial of the number.

# Problem Constraints
# 1 <= A <= 100

# Input Format
# First and only argument is the integer A.
# Output Format
# Return a string, the factorial of A.

# Input: 3
# Output: 6
# asked in: BrowserStack

class SOlution:
    
    # @param A: integer
    # @return a string

    def solve(self, A):
        if A == 1 or 0:
            pass
        else:
            A = A * (A - 1)
            return A