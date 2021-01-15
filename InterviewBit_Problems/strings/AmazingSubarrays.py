# Given string s, have to find all substrings of S.

# Output: Return a single integer X mod 10003, here X is the number of amazing subarrays in given strings.

# Constraints:

# 1 <= length(S) < 1e6
# S can have special characters

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        ans = 0
        for i in range(len(A)):
            if A[i] in vowels:
               ans = ans + (len(A) - i)%10003
        return ans%10003