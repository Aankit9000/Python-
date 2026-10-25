# # User input
name = input("Enter your name: ")
print(f"Hello {name}")
age = input("Enter your age: ")
age = int(age)
age = age + 67
print(f"You are {age} years old")

#mad libs

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")

print(f"Today I went to a {adjective} zoo")
print(f"In an exhibit, I saw {noun}")

#area calc

length = float(input("Enter the length of a rectangle: "))
width = float(input("Enter the width of a rectangle: "))
height = float(input("Enter the height of a rectangle: "))
area = length * width * height
print(f"The area of the rectangle is {area}cm^3")