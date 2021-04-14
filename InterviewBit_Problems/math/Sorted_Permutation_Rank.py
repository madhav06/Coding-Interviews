# Python 3 code

'''
Given a string, find the rank of the string amongst its permutations sorted lexicographically.
Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba

'''

import math
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        A = list(A)
        chars = A[:]
        chars.sort()
        count = 0
        i = 0
        while i < len(A):
            index = chars.index(A[i])
            if index != 0: 
                count += math.factorial(len(A)-i-1)*index
            else:
                if chars[i:] == A[i:]:
                    break
            chars.pop(index)
            A.pop(i)
        return (count+1)%1000003

        