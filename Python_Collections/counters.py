# A Python Program to show differetn ways to create counter

from collections import Counter

# with sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C']))

# with dictionary
print(Counter({'A': 3, 'B':5, 'C':2}))

# with keywords args
print(Counter(A=3, B=5, C=2))