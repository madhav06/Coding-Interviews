# 1 is read off as one 1 or 11.
# 11 is read off as two 1s or 21.

# 21 is read off as one 2, then one 1 or 1211.

# Given an integer n, generate the nth sequence.

# Note: The sequence of integers will be represented as a string.

# Example:

# if n = 2,
# the sequence is 11.

class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        numbers = [1] #Stores list of numbers
        for i in range(A-1):
            count = 1
            counts = []
            for j in range(len(numbers)):
                # Handle last element case
                if j == len(numbers) - 1: 
                    counts.append(count)
                    counts.append(numbers[j])
                    break
                #Increment count for matching elements
                if numbers[j] == numbers[j+1]:
                    count += 1
                else:
                    counts.append(count)
                    counts.append(numbers[j])
                    count = 1
            
            numbers = counts   
                    
                 
    
        return "".join([str(x) for x in numbers])