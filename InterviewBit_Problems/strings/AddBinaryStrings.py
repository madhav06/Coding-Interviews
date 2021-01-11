# Python 3

class Solution:
    # @param A
    # @param B
    # @return string

    def addBinary(self, A, B):
        A = int(A, 2)
        B = int(B, 2)
        A = A + B

        a = bin(A).replace('0b','')
        return a