#pythons

# Given a string A and integer B, remove all consecutive same characters that have length exactly B.

# Input: A = aabcd
#        B = 2

# Output: bcd


class Solution:
    def solve(self, A, B):
        n = len(A)
        ans = ""
        i = 0
        j = 0
        count = 0

        while j < n:
            while (j < n) and (A[j] == A[i]):
                count += 1
            if count != B:
                ans = ans + A[i:j]
            
            i = j
            count = 0
        return ans
