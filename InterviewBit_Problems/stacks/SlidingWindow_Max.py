"""
 Time:  O(n)
 Space: O(k)

 Given an array nums, there is a sliding window of size k
 which is moving from the very left of the array to the
 very right. You can only see the k numbers in the window.
 Each time the sliding window moves right by one position.

 For example,
 Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

 Window position                Max
 ---------------               -----
 [1  3  -1] -3  5  3  6  7       3
  1 [3  -1  -3] 5  3  6  7       3
  1  3 [-1  -3  5] 3  6  7       5
  1  3  -1 [-3  5  3] 6  7       5
  1  3  -1  -3 [5  3  6] 7       6
  1  3  -1  -3  5 [3  6  7]      7
 Therefore, return the max sliding window as [3,3,5,5,6,7].

 Note: 
 You may assume k is always valid, ie: 1 <= k <= input array's size for non-empty array.

Follow up:
 Could you solve it in linear time?
"""



from collections import deque

class Solution():
    def slidingMaximum(self, A, B):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()
        max_numbers = []

        for i in range(len(A)):
            while dq and A[i] >= A[dq[-1]]:
                dq.pop()
            dq.append(i)
            if i >= B and dq and dq[0] <= i - B:
                dq.popleft()
            if i >= B - 1:
                max_numbers.append(A[dq[0]])

        return max_numbers