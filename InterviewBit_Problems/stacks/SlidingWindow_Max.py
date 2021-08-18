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
    def slidingMaximum(self, arr, B):
        """
        A : Array
        B : Window Size
        """
        n =len(arr)
        dq = deque()
        max_numbers = []

        # Stage 1
        for i in range(B):
            while(len(dq) > 0 and arr[dq[-1]] < arr[i]):
                dq.pop() # remove from rear
            dq.append(i) # add to rear

        # Stage 2
        for i in range(B, n):
            max_numbers.append(arr[dq[0]])
            while(len(dq) > 0 and dq[0] <= i-B):
                dq.popleft() # remove from the front
            while(len(dq) > 0 and arr[dq[-1]] < arr[i]):
                dq.pop() # remove from rear
            dq.append(i) # add to rear
        max_numbers.append(arr[dq[0]])

        return max_numbers

    print(slidingMaximum([9,6,11,8,10,5,4,13,93,14], 4))