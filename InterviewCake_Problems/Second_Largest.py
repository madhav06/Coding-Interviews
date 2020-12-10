# python3
# Program to find the second largest number in list:

a = []

n = int(input("Enter total numbers: "))

for i in range(1, n+1):
    b = int(input("Enter number: "))
    a.append(b)
    a.sort()

print("Second largest number is: ", a[n-2])