# Input 1:
#     A = "ABC"
# Output 1:
#     2
#     Explanation 1:
#         Insert 'B' at beginning, string becomes: "BABC".
#         Insert 'C' at beginning, string becomes: "CBABC".

# Input 2:
#     A = "AACECAAAA"
# Output 2:
#     2
#     Explanation 2:
#         Insert 'A' at beginning, string becomes: "AAACECAAAA".
#         Insert 'A' at beginning, string becomes: "AAAACECAAAA".


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if A == A[::-1]:
            return 0
        j = len(A) - 1
        while j >= 0:
            B = A[:j]
            if B == B[::-1]:
                return len(A) - j
            j -= 1
        return len(A) - 1