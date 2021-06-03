# Python 2


# Implement pow(x, n) % d.

# In other words, given x, n and d,

# find (xn % d)

# Note that remainders on division cannot be negative.
# In other words, make sure the answer you return is non negative.

# Input : x = 2, n = 3, d = 3
# Output : 2

# 2^3 % 3 = 8 % 3 = 2.

class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        
        res = 1 % d  # Cover case d == 1
        while n > 0:
            if n & 1:   # Odd?
               res = (res * x) % d
            x = x**2 % d
            n >>= 1
        return res