# python3
# pyhton program to check if a string is a palindrome or not

string = raw_input("Enter string")
if(string == string[::-1]):
    print("The string is palindrome.")
else:
    print("The string isn't palindrome.")