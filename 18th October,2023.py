# Task1
"""Take an input and print the Series.
Fibonacci Series
"""

num=int(input("Enter the Number:"))
a=0
b=1

for i in range(0,num):
    print(a, sep=" ", end="\t")
    c = a + b
    a = b
    b = c
print("\n")

# Factorial Series
import math
number=int(input("Enter the Number:"))
print("The Factorial of the Given Number is:")
print(math.factorial(number))
print("\n")
# Task 2
"""Using Break to exit a loop when i==51 while 
printing the values from 1 to 100"""
for i in range(1,100):
    print(i,end="\t")
    if i==51:
        break


