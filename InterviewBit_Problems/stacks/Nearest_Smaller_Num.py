# Python3 Code

# algorithm to find smaller element
# on left side
 
# Prints smaller elements on left
# side of every element
def printPrevSmaller(arr, n):
 
    # Always print empty or '_' for
    # first element
    print("_, ", end="")
 
    # Start from second element
    for i in range(1, n ):
     
        # look for smaller element
        # on left of 'i'
        for j in range(i-1 ,-2 ,-1):
         
            if (arr[j] < arr[i]):
             
                print(arr[j] ,", ",
                            end="")
                break
 
        # If there is no smaller
        # element on left of 'i'
        if (j == -1):
            print("_, ", end="")
 
# Driver program to test insertion
# sort
arr = [1, 3, 0, 2, 5]
n = len(arr)
printPrevSmaller(arr, n)