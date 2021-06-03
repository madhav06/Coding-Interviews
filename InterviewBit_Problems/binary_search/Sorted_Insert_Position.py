# Problem Description

# Given a sorted array A and a target value B, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.



# **Problem Constraints**
# 1 <= |A| <= 100000

# 1 <= B <= 109



# **Input Format**
# First argument is array A.

# Second argument is integer B.



# **Output Format**
# Return an integer, the answer to the problem.

def bisect_left(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo


class Solution:
    def searchInsert(self, arr, target):
        return bisect_left(arr, target)