#Task1
"""Write a Python Program to find the largest number in a list"""
my_list=[55,100,35,76,80]
print(max(my_list))

#Task2
"""Write a Python Program to find the smallest number in a list"""
my_list=[55,100,35,76,80]
print(min(my_list))

#Task3
"""Write a Python Program to sum all the numbers in a list"""
new_list=[1, 2, 3, 4, 5]
print(sum(new_list))

#Task4
"""Write a Python Program to multiply all the numbers in a list"""
def multiply_ele(newlist):
    prod=1
    for i in newlist:
        prod=prod*i
    return prod
newlist=[1, 2, 3, 4, 5]
print("The multiplication of all the elements of the list is:",multiply_ele(newlist))

#Task5
"""Write a Python Program to count the number of a string in a list 
where the string length is 2 or more and the first and last charecter are the same."""
def match_words(words):
    ctr=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
           ctr+=1
    return ctr
print(match_words(['abc','xyz','aba','1221']))