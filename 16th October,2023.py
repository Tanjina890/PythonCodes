# TASK 1
"""Grade Calculator
Write a program that calculates and displays the letter grade for a given
numerical score(eg: A,B,C,D,F)based on the following grading scale
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59"""

score=int(input("Enter the Score:"))
if score>=90 and score<=100:
    print("A grade")
elif score>=80 and score<=89:
    print("B Grade")
elif score>=70 and score<=79:
    print("C Grade")
elif score>=60 and score<=69:
    print("D Grade")
else:
    print("F Grade")

# TASK 2
"""Create a Program that determines whether a given Year is a Leap Year.
A leap year is Divisible by 4,but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination"""

year=int(input("Enter the Year:"))
if year%4==0 or year%400==0 and year%100!=0:
    print("The Year is Leap Year.")
else:
    print("The Year is not Leap Year.")

# TASK 3
"""Write a Program that classifies a triangle based on its side lengths
Given three input values representing the lengths of the sides,
determine if the triangle is equilateral(all sides are equal)
isosceles(exactly two sides are equal) or scalene(no sides are equal).
Use an if-else statement to classify the triangle.
"""
side1=int(input("Enter the Value of Side1:"))
side2=int(input("Enter the Value of Side2:"))
side3=int(input("Enter the Value of Side3:"))
if side1==side2==side3:
    print("The Triangle is equilateral")
elif side1==side2 or side2==side3 or side3==side1:
    print("The Triangle is Isosceles")
else:
    print("The Triangle is Scalene.")
