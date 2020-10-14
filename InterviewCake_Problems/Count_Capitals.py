# Python 2.7

# Write a one-liner that will count the number of capital letters in a file. Your code should work
# even if the file is too big to fit in memory.

## this code will implement the desired logic, but it's not one-liner.

# with open(SOME_LARGE_FILE) as fh:
# 	count = 0

# 	for line in fh:
# 		for character in line:

# 			count += (1 if character.isupper() else 0)

## python3 didn't have a function to count capital letters, but it does have a function to add up bunch of 1's and 0's.: sum().

count = sum(1 if character.isupper() else 0 for line in fh for character in line)

# or

count = sum(character.isupper() for line in fh for character in line)