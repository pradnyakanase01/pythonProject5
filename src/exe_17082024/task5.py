### Task #5
"""

- Create a program that takes two numbers as input and prints whether the first number is greater than,
less than, or equal to the second number.

"""
num1 = int(input("Enter first Number  "))
num2 = int(input("Enter second number  "))

if (num1 == num2):
    print(num1,"=",num2)

elif(num1 >num2):
    print(num1, '>',num2)

else:
    print(num2,'>',num1)