# python3
# python program to to common letters in two input strings:

s1 = raw_input("Enter first string: ")
s2 = raw_string("Enter second string: ")

a = list(set(s1)&set(s2))

print("The common letters are: ")
for i in a:
    print(i)