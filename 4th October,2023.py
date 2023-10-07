#TASK1

name=input("Enter the Name of the User:")
print(name)

#TASK2

name1=input("Enter the First Name:")
name2=input("Enter the Last Name:")
#print(name1,name2,sep="_",end="\t")
print(name1+"_"+name2)

#TASK3

name3=input("Enter The User Name:")
#a="You are Welcome"
#b="To the Python Class"
#print(a,name3,b)
print("You are Welcome" " "+name3+" " "To the Python class")
#_________________
#TASK3
name3=input("Enter The User Name:")
a="You are Welcome <{}> To the Python Class"
print(a.format(name3))
