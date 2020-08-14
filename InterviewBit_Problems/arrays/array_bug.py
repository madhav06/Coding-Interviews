# The following code is supposed to rotate the array A by B positions.

# So, for example,


# A : [1 2 3 4 5 6]
# B : 1

# The output :

# [2 3 4 5 6 1]
# However, there is a small bug in the problem. Fix the bug and submit the problem.

class Solution:
    # @param a: list of integers
    # @param b: integers
    # @return a list of integers
    def rotateArray(self, a, b):
        # if b > len(a): b = b%len(a)
        for i in xrange(b%len(a)):
            first = a.pop(0)
            a.append(first)

        return a
