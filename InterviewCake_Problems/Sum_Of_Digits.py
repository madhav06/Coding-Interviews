# Python3

# Python Program to find sum of digits of a number

n = int(input(" Enter a number: "))

sum_of_digit = 0

while(n > 0):
    digit = n % 10
    sum_of_digit = sum_of_digit + digit
    n = n // 10

print("The sum of digits: ", sum_of_digit)