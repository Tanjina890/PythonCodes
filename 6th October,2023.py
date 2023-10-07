#Task2 String Format
language="Python"
centre="TestingAcademy"
print(f"I'm learning {language} from {centre}.")

#-----OR------
language="Python"
centre="TestingAcademy"
txt="Hello Everyone!!!\nI'm Learning {} from{}"
print(txt.format(language,centre))

#Task2 Table
num=int(input("Enter the Number\n"))
for i in range(1,11):
    print(num,'X',i,'=',num*i)

#Task3
txt1="Hello Python"
print(len(txt1))

#Task3 Functions in String Data Type
txt1="Hello,Python_"
print(len(txt1))
print(txt1.upper())
print(txt1.lower())
print(txt1.replace("P","J"))
print(txt1.split(","))
print(txt1.swapcase())
print(txt1.capitalize())
print(txt1.casefold())
print(txt1.isnumeric())
print(txt1.endswith("_"))
print(txt1.isalnum())
print(txt1.isalpha())
print(txt1.isascii())
print(txt1.istitle())
print(txt1.isupper())