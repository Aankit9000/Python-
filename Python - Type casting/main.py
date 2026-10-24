# typecasting = The process of converting one data type to another
#               (String, integer, float, boolean)
#               Explicit vs implicit

#Explicit typecasting

name = "Anakin Skywalker"
age = 67
power_level = 6.7
jedi = True

print(type(name))

name = bool(name)
print(name)
print(type(name))

# implicit

x = 6
y = 6.7

xy = x/y
print(xy)
print(type(xy))
