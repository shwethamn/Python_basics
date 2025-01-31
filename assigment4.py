'''
Logical Operator Practice:
Write a Python program that takes two numbers as input from the user and checks if:
Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).
'''
'''
a=int(input("enter the Number1:  "))
b=int(input("enter the Number2:  "))
c=10
if a > c and b > c:
    print("Both numbers are greater than 10")

if a < 5 or b < 5:
    print("At least one number is less than 5")

if not a > b:
    print("first number is not greater than the second")
else:
    print("second number is not greater than the first")
'''
'''
Comparison Operator Challenge: 
Create a Python program that asks the user for their age and prints:
"You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.
'''
'''
age=int(input("Please enter your age:  "))
if age >= 18:
    print("You are an adult")
else:
    print ("You are a minor")
'''
'''Membership Operator Exercise: Write a Python program that:

Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in).
'''
'''
string=input("Enter any string: ")
print('a' in string)
print('Python' not in string)
'''

'''
Given two integers, write a Python program that:

Prints the result of a & b, a | b, and a ^ b.
Shifts the bits of a two positions to the left (a << 2).
Shifts the bits of b one position to the right (b >> 1).
'''
a=10
b=5
print(a&b)
print (a|b)
print(a^b)
print(a<<2)
print(b>>1)

string="shwetha"
print(string[::-1])  #uses slicing ([::-1]