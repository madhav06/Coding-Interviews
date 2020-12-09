# Python3
# Python program to check if number is armstrong or not

n = int(input("Enter any number: "))

a = list(map(int, str(n)))

b = list(map(lambda x: x**3, a))

if(sum(b) == n):
    print("The number is Armstrong number ! ")
else:
    print("The number isn't an Armstrong number !")