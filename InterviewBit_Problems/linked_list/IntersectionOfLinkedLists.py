# Asked in NetApp, Microsoft, Amazon

# write a program to find the node at which the ,
# intersection of two LL begins.

class Solution:
    def length(self,A):
        count = 0
        while A:
            count += 1
            A = A.next
        return count

    def getIntersectionNode(self,A,B):
        m = self.length(A)
        n = self.length(B)

        d = n-m
        if m > n:
            temp = A
            A = B
            B = temp
            d = m-n

        c = 0
        while c < d:
            B = B.next
            c += 1
        while B and A:
            if A == B:
                return A
            A = A.next
            B = B.next
        return None