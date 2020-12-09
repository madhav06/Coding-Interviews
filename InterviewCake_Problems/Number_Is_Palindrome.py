# Python3

# Python Program to check palindrome or not

n = int(input("Enter number: "))

temp = n
reverse = 0
while(n > 0):
     digit = n % 10
     reverse = reverse* 10+digit
     n = n // 10

if (temp == reverse):
    print("The number is palindrome!")
else:
    print("The number isn't palindrome!")

