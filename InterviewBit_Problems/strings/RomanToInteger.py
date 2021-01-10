# Given a string A representing a roman numeral.
# Convert A into integer.

# A is guaranteed to be within the range from 1 to 3999.

# Input: A = XIV, Output: 14

# Input: A = XX, Output: 20

class Solution:
    # @param A
    # @return integer
    def romanToInt(self, A):

        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        prev = 0
        for char in A:
            result = result + d[char]
            if d[char] > prev:
                result = result - 2* prev
            prev = d[char]

        return result;
