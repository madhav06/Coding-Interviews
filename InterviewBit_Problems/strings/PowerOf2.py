# Find if Given number is power of 2 or not.
# More specifically, find if given number can be expressed as 2^k where k >= 1.

# Input:

# number length can be more than 64, which mean number can be greater than 2 ^ 64 (out of long long range)
# Output:

# return 1 if the number is a power of 2 else return 0

# Example:

# Input : 128
# Output : 1

class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        if int(A[-1]) % 2:
            return 0

        binary = '{:b}'.format(int(A))

        for b in binary[1:]:
            if b != '0':
                return 0
        return 1