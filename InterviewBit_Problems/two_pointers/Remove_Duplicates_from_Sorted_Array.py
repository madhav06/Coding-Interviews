# python 3 code

'''
Remove duplicates from Sorted Array
Given a sorted array, remove duplicates in place such that element appears only once and return
the new length

Do not allocate the extra space for another array, must do in place with constant memory

Given array: [1, 1, 2]
function should return length = 2, A = [1, 2]
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=0
        j=i+1
        while(j<len(A)):
            if(A[i]==A[j]):
                j+=1
            else:
                i+=1
                A[i]=A[j]
        A=A[:i+1]
        return i+1

