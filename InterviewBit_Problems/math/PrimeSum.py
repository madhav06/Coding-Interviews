# Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

# NOTE A solution will always exist. read Goldbach’s conjecture

# Example:


# Input : 4
# Output: 2 + 2 = 4

# If there are more than one solutions possible, return the lexicographically smaller solution.

# If [a, b] is one solution with a <= b,
# and [c,d] is another solution with c <= d, then

# [a, b] < [c, d] 

# If a < c OR a==c AND b < d.

import math
class Solution:
    def isPrime(self,n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        for i in range(2,(A//2)+1):
            # che cking with AND Op
            if self.isPrime(i) and self.isPrime(A-i):
                return (i,A-i)
        return (0,0)