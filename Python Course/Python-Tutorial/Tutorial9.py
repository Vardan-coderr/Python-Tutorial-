# # # Conditional Statements in Python 

# # # 1. if statement :- 
# # # Example of if statement in python :-

# # # a = 33
# # # b = 200
# # # if (b > a):
# # #     print("b is greater than a")
            
# # # 2. if...else statement :-
# # # Example of if...else statement in python :-

# # # a = int(input("Enter Your age :"))
# # # if (a > 18):
# # #     print("You Can Drive")
# # # else:
# # #     print("You Can't Drive")
    
# # # 3. if...elif...else statement :-
# # # Example of if...elif...else statement in python :-

# # # num = int(input("Enter the Value of Num :"))
# # # if ( num < 0):
# # #     print("Number is Negative")
# # # elif (num == 0) :
# # #     print(" NUmber is Zero")
# # # elif (num == 999) :
# # #     print(" Number is Special")
# # # else:
# # #     print("Number is Positive")
# # # print("I am Happy Now")     
    
# # # 4. nested if statement :- We can use if...else statement inside another if...else statement. This is called nested if statement.
# # #  Example of nested if statement in python :-
# # # num = 18
# # # if(num<0):
# # #     print("Number is Negative")
# # # elif(num>0):
# # #     if(num<=10):
# # #         print("Number is between 1-10")
# # #     elif(num>10 and num<=20):    
# # #         print("Number is between 10-20")
# # #     else:
# # #         print("Number is zero")
# # # print("I am Happy Now")


# # # Match Case Statements in Python :-
# # # A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.
# # # Syntax of match case statement in python :-
# # match variable_name:
# #             case ‘pattern1’ : //statement1
# #             case ‘pattern2’ : //statement2
# #             …            
# #             case ‘pattern n’ : //statement n

# #  example of match case statement in python :-

# day = int(input("Enter the Day Number :"))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid Input")

# # # Note :- The underscore (_) case is a wildcard that matches anything. It acts like the default case in a switch statement in other programming languages.
 


    