# We want to build a matrix of values, like a multiplication table. the output we want should be list of lists, like:

# [[1,2,3], [2,4,6], [3,6,9]]

iterator = [i for i in range(1, 4)]
matrix = [[x * y for y in iterator] for x in iterator]