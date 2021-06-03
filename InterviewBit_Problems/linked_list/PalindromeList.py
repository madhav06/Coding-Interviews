

# Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its palindrome or not.

# Expecting solution in a linear constant period of time

# for example:
#     List 1 --> 2 --> 1 is a palindrome.
#     List 1 --> 2 --> 3 is not a palindrome.

class Solution:
    # @param A: head node of linked list
    # @return an integer
    def lPalin(self,A):

        a = []
        while(A != None):
            a.append(A.val)
            A = A.next
        
        arev = a[::-1]
        if (arev == a):
            return 1
        else:
            return 0

