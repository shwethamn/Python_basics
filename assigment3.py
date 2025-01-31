#problem 1
'''
Write a Python program that asks the user to input their name and age,
then prints a greeting message that includes their name and how old they will be in 5 years
'''
'''
name=input("Name: ")
age=int(input("Age: "))
age_5_yr=age + 5
print(f"Hello! {name} In 5 years your age is {age_5_yr}")
'''

#problem 2
'''
Write a Python program that asks the user to input two numbers and 
then prints the sum, difference, product, and quotient of those two numbers
'''
a=int(input("Number1:  "))
b=int(input("Number2:  "))
#print (a+b)
#print (a-b)

#problem 3:
'''
 Write a Python program that asks the user for their name and age, then prints a personalized greeting message. 
 Use both the + operator and f-strings for output.
 Enter your name: Alice
Enter your age: 25
Output: Hello, Alice! You are 25 years old.
'''

name=input("Enter your Name: ")
age=input("Enter your  Age: ")
print(f"Hello,{name}! You are {age} years old")


'''
String Manipulation Exercise: Write a Python program that:

Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.
Input: "   Python is awesome!   "
Output:
Uppercase: "PYTHON IS AWESOME!"
Lowercase: "python is awesome!"
Replaced: "___Python_is_awesome!___"
Stripped: "Python is awesome!"
'''

sentence=input("Enter the sentence: ")
print(f"Upper case: {sentence.upper()}")
print(f"Upper case: {sentence.lower()}")
print(f"Stripped: {sentence.strip()}")
print(f"Upper case: {sentence.replace(" " , "__")}")


'''
Character Counter: Write a Python program that:

Asks the user for a string.
Prints how many characters are in the string, excluding spaces.
Input: "Hello World"
Output: "Number of characters (excluding spaces): 10"'''


string=input("Enter the string: ")
print(string[0:])
print(f"Number of characters {len(string)}")