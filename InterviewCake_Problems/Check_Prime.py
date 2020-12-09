# python3
# Python Program to check if a number is prime?

num = int(input("Enter number: "))

if num > 1:
    for i in range(2, num//2):
        if (num%i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
        
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")