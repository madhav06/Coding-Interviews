# Python3

# Given a sorted array of integers, find the number of occurrences of a given target value.
# Your algorithm’s runtime complexity must be in the order of O(log n).
# If the target is not found in the array, return 0

# **Example : **
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return 2.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        
        def search(A, B, searchFirst = True):
            low = 0
            high = len(A) - 1
            result = -1
            while low <= high:
                mid = low + (high-low)//2
                if A[mid] == B:
                    result = mid
                    if searchFirst:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif A[mid] < B:
                    low = mid + 1
                else:
                    high = mid - 1
            return result
            
        first_element = search(A,B)
        last_element = search(A,B,False)
        if first_element == -1:
            return 0
        else:
            return last_element - last_element +1