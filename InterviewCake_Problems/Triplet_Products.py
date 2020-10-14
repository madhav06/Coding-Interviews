# Maximum product of triplets (subseq of size 3)

# Given an integer array, find a maximum product of a triplet in a array.

# Input: [10,3,5,6,10]

# Output: 1200


# function to find a maximum product of a triplet in array of integers of size n


def maxProduct(arr, n): 
 
    # if size is less than 3, no triplet exists 
    if n < 3:
        return -1
 
    # Sort the array in ascending order 
    arr.sort()
 
    # Return the maximum of product of last 
    # three elements and product of first 
    # two elements and last element 
    return max(arr[0] * arr[1] * arr[n - 1], 
               arr[n - 1] * arr[n - 2] * arr[n - 3]) 
 
# Driver Code
if __name__ == "__main__":
 
    arr = [-10, -3, 5, 6, -20] 
    n = len(arr) 
 
    _max = maxProduct(arr, n) 
 
    if _max == -1: 
        print("No Triplet Exists") 
    else:
        print("Maximum product is", _max) 

