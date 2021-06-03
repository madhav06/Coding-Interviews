# Python 3 Code

'''
Given an array and a value, remove all the instances of that value in the array.
Also, return the number of elements left in the array after the operation.
It doesn't matter what is left beyond the expected length then


Examle:

A = [4, 1, 1, 2, 1, 3]

and value elem = 1

then new length is 3. A is now = [4, 2, 3]
'''

class Solution:
    # @param A: list of integers
    # @param B: integer
    # @return an integer

    def removeElement(self, a, num):
        n = len(a)
        checkpoint = 0

        for i in range(n):
            if a[i] != num:
                a[i], a[checkpoint] = a[checkpoint], a[i]
                checkpoint = checkpoint + 1
        return checkpoint
