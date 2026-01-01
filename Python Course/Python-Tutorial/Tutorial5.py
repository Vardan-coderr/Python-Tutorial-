# In these tutorials, we will learn about TypeCasting in python 
# TypeCasting is the conversion of one data type to another data type
# There are two types of TypeCasting in python  
# 1. Explicit TypeCasting
# 2. Implicit TypeCasting
# Explicit TypeCasting is done by the user manually
# Implicit TypeCasting is done by the python interpreter automatically

# Example of Explicit TypeCasting

a = 1 # here a is an integer
b = "2" # here b is a string
print( int(a) + int(b)) # here we are converting b to integer and then adding it to a

# Example of Implicit TypeCasting
c = 2.3 # here c is a float
d = 5 # here d is an integer
print( c + d ) # here d is converted to float and then added to c automatically by our intreptor

# simple program 
string = "15"
number = 7
str_num = int(string) 
sum = number + str_num
print("The sum of the string and number is:", sum )


# if you want to konw about what type of data is stored in varibale so you can use type() function
a = 5
print(type(a))
b = 16.5
print(type(b))
sum = a + b
print("The sum of a and b is:", sum)
print(type(sum))  