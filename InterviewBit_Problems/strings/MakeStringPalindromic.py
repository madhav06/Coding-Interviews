
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
        # A palindromic string is equal to its reverse
        reverse = A[::-1]
        if reverse == A:
            return 0
            
        # Every string can be made a palindrome by prepending
        # (or appending) the reverse, and the outermost letter
        # can be ignored. An initial part of the reverse might
        # suffice if there are duplicate letters, so just count
        # how much of the reverse we need:
        for i in range(1, len(reverse)):
            if reverse[:i] + A == reverse + A[-i:]:
                break
        return i