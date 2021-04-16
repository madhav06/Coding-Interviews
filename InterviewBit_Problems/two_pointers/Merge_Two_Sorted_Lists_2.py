# python 3 Code

'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

if the number of elements initialize in A and B are m and n respectively, the resulting size of array A 
after code executed is m+n.

Example: A = [1, 5, 8] B = [6,9]

Modified A = [1, 5, 6, 8, 9]

'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        A.extend(B)
        A.sort()
        return A

