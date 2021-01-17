# Python3

# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Given s = "Hello World",

# return 5 as length("World") = 5.

# Please make sure you try to solve this problem without using library functions. Make sure you only traverse the string once.

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        count = 0
        
        for i in A[::-1]:
            if count == 0 and i == " ":
                pass
            elif count != 0 and i == " ":
                return count
            else:
                count = count + 1
        return count
