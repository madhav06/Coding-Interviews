# Problem Description

# Given a string A consisting of lowercase characters.

# You have to find the number of substrings in A which starts with vowel and end with consonants or vice-versa.

# Return the count of substring modulo 109 + 7.

# Input Format
# First argument is an string A.



# Output Format
# Return a integer denoting the the number of substrings in A ,
# which starts with vowel and end with consonants or vice-versa with modulo 109 + 7.

# Example Input
# Input 1:

#  A = "aba"
# Input 2:

#  A = "a"


# Example Output
# Output 1:

#  2
# Output 2:

#  0

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count_v = 0
        count_c = 0
        
        for c in A:
            if c in vowels:
                count_v += 1
            else:
                count_c += 1

        return (count_v * count_c) % 1000000007
