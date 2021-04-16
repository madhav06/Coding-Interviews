# Python 3 Code

'''
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length

Do not allocate extra space for another array, you must do this in place with constant memory

example
input array = A = [1, 1, 1, 2]

return len = 3, A = [1, 1, 2]
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 2
        variable = 2
        while i < len(A):
            if A[variable - 1] != A[i] or A[variable - 2] != A[i]:
                A[variable] = A[i]
                variable += 1
            i += 1
        return variable

        

