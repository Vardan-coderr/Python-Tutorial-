# In These Tutorial we learn about Python Variables and Data Types :-

# Variables :- Variables are used to store data in a program. In Python, we don't need to declare a variable before using it. We can simply assign a value to a variable and it will be created automatically.

# Data Types :- Data types are used to define the type of data that a variable can store. In Python, there are several built-in data types such as:
# 1. int :- It is used to store integer values. 
# 2. float :- It is used to store floating-point values.
# 3. str :- It is used to store string values.
# 4. bool :- It is used to store boolean values (True or False).
# 5. list :- It is used to store a collection of values.
# 6. tuple :- It is used to store a collection of values that cannot be changed
# 7. dict :- It is used to store a collection of key-value pairs.
# 8. set :- It is used to store a collection of unique values.
# 9. complex :- It is used to store complex numbers.
# 10. NoneType :- It is used to represent the absence of a value

# Example of Variables and Data Types in Python :-
    
a = 1 #integer 
print(a)
print("The type of a is :",type(a))

b = "Hello Vardan" # string
print(b)
print("The type of b is :",type(b))

c = True #bollen
print("The type of c is :",type(c))

d= complex(2+2) #complex
print("The type of d is :",type(d))

list1 = [[2,7,290.022] , ["apple","banana"]] 
print(list1,type(list1)) #list

tuple1 = (("Vardan","veer"),(1,23,7,16))
print(tuple1,type(tuple1)) #tuple

dict1 = {"Name": "vardan","age": 20 ,"canVote": "True"}
print(dict1,type(dict1))






