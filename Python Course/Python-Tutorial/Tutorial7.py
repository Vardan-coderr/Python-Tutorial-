# # In these tutorail we learn about string in python
# # A string is a sequence of characters enclosed in single or double quotes
# # You can use single quotes or double quotes to create a string
# # Example of string in python :-
# str1 = 'Hello World' # string enclosed in single quotes
# str2 = "Hello World" # string enclosed in double quotes
# print(str1)
# print(str2)


# # Multi line string in python :-
# # In Python , we can create a multi line string by using triple quotes (''' or """)
# str = """Hello Everyone  
# Welcome to Python Programming
# This is a multi line string
# """
# print(str)

# # Accessing of characters in a string :-
# # In Python , string is like an array (array is collection of items ) of characters . we can access the characters of a string using indexing
# # which starts from 0 
# # sqaure brackets are used to access the characters of a string
# name = "Vardan"
# print(name[0]) # it will print the 0  index character of the string

# # Looping through a string :-
# # using for loop we can loop through each character of the string
# for character in name:
# print(character)
    
# # string slicing :-
# # we can get a substring from a string by using slicing
# names = "Vardan,veer"
# print(name[0:6]) # it will print the characters from index 0 to 6 (6-1)
# # example of slicing
# fruit = "mango"
# len1 = len(fruit)
# print("Mango is a ",len1,"letter word") # it will print the length of the string

# # string length
# # we can get the length of a string by using len() function
# print(len(names)) # it will print the length of the string

# lets take some example 

# fruit = "Mango"
# mangolen = len(fruit)
# print(mangolen)
# print(fruit[0 :4]) # it will print the characters from index 0 to 4 (4-1) {0 is strating index and 4 is end index}
# # 0 (4-1) = 0 to 3 it will print from 0 to 3
# print(fruit[:4]) # python interpreter will consider it as (0 to 4)
# print(fruit[:])   # it will print the whole string
# print(fruit[0:len(fruit)-3])
# print(fruit[0:4]) #including 0 but not 4
# print(fruit[1:4]) #including 1 but not 4
# print(fruit[-2:-1]) #inluding -2 but not -1 = 5-2= 3 to 5-1=4 = 3:4
