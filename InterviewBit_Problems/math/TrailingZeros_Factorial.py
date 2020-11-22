# Problem Description

# Given an integer A, return the number of trailing zeroes in A!.

# Note: Your solution should be in logarithmic time complexity.



# **Problem Constraints**
# 1 <= A <= 10000



# **Input Format**
# First and only argumment is integer A.



# **Output Format**
# Return an integer, the answer to the problem.




class Solution:
	# @param A : integer
	# @return an integer
    def trailingZeroes(self, A):
        # Zero is formed by 2*5. 
        # No. of 2's always > No. of 5's in factorial of a number.
        # Therefore, counting the No. of 5's gives the number of trailing zeros
        # If A < 5 then its factorial doesn't have any trailing zeros
        if A < 5:
            return 0
        count = 0
        i = 5
        while(A//i > 0):
            count += A // i
            i *= 5
        return count