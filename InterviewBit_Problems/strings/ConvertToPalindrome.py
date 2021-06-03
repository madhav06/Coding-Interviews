# Python3

# Given a string A consisting only of lowercase characters, 
# we need to check whether it is possible to make this string a palindrome after removing exactly one character from this.

# If it is possible then return 1 else return 0.

# Input: "abcba"

# Output: 1

# Input: "abecbea"

# Output: 0

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if(A==A[::-1]):
            return(1)
        i=0
        j=len(A)-1
        while(j>=i):
            if(A[i]!=A[j]):
                str1=A[i+1:j+1]
                str2=A[i:j]
                if(str1==str1[::-1] or str2==str2[::-1]):
                    return(1)
                else:
                    return 0
            i+=1
            j-=1
        return(0)