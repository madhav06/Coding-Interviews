# Python3

# Given a string A consisting of lowercase characters.

# We need to tell minimum characters to be appended ,
# (insertion at end) to make the string A a palindrome.


def ispal(A,i,j):
    c=0
    
    while i<j:
        if A[i]!=A[j]:
            return 0
        i+=1
        j-=1
    return 1


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        i=0
        j=len(A)-1
        c=0
        
        while i<j:
            if A[i]==A[j]:
                if ispal(A,i,j):
                    return c
            i+=1
            c+=1
            
        return c
            
            