# Python3
# Python Program to Count the number of digits in a number

n = int(input("Enter number: "))
count = 0

while( n > 0 ):
    count = count + 1
    n = n // 10
p[rint(" The number of digits in the number is: ", count)