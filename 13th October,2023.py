# Task 2
"""Write a Python program to Calculate
the Area of a Circle given it's radius using the formula
area=Pixr^2(Take Pie as 3.14)"""

radius=float(input("Please enter the Radius of the Circle:"))
area=3.14*radius*radius
#area=3.14*(radius**2)
print("The area of the Circle is:",area)

"""Create a program that takes two numbers as input and prints whether
 the first number is greater than,less than,or equal to the second number"""

first_num=int(input("Enter the First Number:"))
second_num=int(input("Enter the Second Number:"))
if first_num>second_num:
    print("First Number is greater than the Second number")
elif first_num<second_num:
    print("First Number is less than the Second number")
else:
    print("First Number is equal to Second number")
#-------------------OR-----------------------------------

first_num=int(input("Enter the First Number:"))
second_num=int(input("Enter the Second Number:"))
result="First Number is Greater than Second Number" if first_num>second_num else "First Number is Less than Second Number" \
    if first_num<second_num else "First Number is equal to Second Number"
print(result)

"""Use the Ternary Operator 
to find the maximum of 
three numbers entered by the User"""

num1=int(input("Enter the First Number:"))
num2=int(input("Enter the Second Number:"))
num3=int(input("Enter the Third Number:"))
max=num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3
print("Maximum value is:",max)

#Task2
"""Develope a Python Script 
that calculates the 
Square and Cube of a Given Number"""
num=int(input("Enter the Number:"))
square=num**2
cube=num**3
print("The Square of the Given Number is:",square)
print("The Cube of the Given Number is:",cube)