# Python3

class Solution:
    # # @param A : list of list of integers
    # # @return an integer
    # def findMedian(self, A):
        
    def findMedian(self, A):
        """Returns the median value from given list"""
        for i in range(1,len(A)):
            A[0].extend(A[i])

        return (sorted(A[0])).pop(len(A[0])// 2)
 

 # Secondary Optimal solution:        
        
# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def findMedian(self, A):

#         def arr_median(arr):
#             # A will be 1D array
#             # the array length is odd
#             arr = sorted(arr)
#             median_index = (len(arr)+1)//2
#             return arr[median_index-1]
            
#         if len(A)==0:
#             return []
        
#         arr = []
#         for row in A:
#             arr.extend(row) 
        
#         return arr_median(arr)