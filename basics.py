


# my_number = 42

# your_guess = 0

# while (your_guess != my_number):

#     your_input = input("Guess my number: ")
#     your_guess = int(your_input)
# if your_guess < my_number:
#         print("guess higher!")
# elif your_guess > my_number: 
          
#             print("guess lower!")
# print("You got it!")


# ----------------------------------------------------------
# print("Starting...")
# count = 0
# while count < 17: # repeat 10 times
#     print(count)
#     count = count + 1
# print("Done!")



# --------------------------------------------------------------------


# def example_3():
#     for count in range(0,10): # we start at 0 and end at 9 (not 10!)
#         print(count)

# example_3()


# ----------------------------------------------------------------------------
# my_number = 42
# while True: # The loop condition is always true
#     your_input = input("Guess my number: ")
#     your_guess = int(your_input)
#     if your_guess == my_number:
#         break # and we break out of the loop here
#     if your_guess < my_number:
#         print("guess higher!")
#     else:
#         print("guess lower!")
# print("You got it!")

# --------------------------------------------------------

# a = 20054
# b = 2007
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# -------------------------------------------------------

# SHORT HAND FOR IF STATEMENTS


# a = 20054
# b = 2007
# if a > b: print("a is greater than b") 

# a = 33
# b = 200

# if b > a:
# having an empty if statement like this, would raise an error without the pass statement
# ------------------------------------------------------------
#  counting in tens till hundred
# x = range(0,101,10)
# for n in x :
#     print(n)

# ----------------------------------------------------------------
# wordlist = ['box','fox','socks',"lox"] # this is an array. It is a simple list of 3 letters.
# for word in wordlist: # item takes on the value of each element in the list, one at a time.
#     print(word)


# my_number = 42
# while True: # The loop condition is always true
#     your_input = input("Guess my number: ")
#     your_guess = int(your_input)
#     if your_guess == my_number:
#         print("You got it!")
#         break # and we break out of the loop here
#     if your_guess < my_number:
#         print("guess higher!")
#     else:
#         print("guess lower!")

# function defining

# def hello(name):
#     print("Hello "+ name)

# hello("B-man")

# ----------------------------------------
# Arbitrary Keyword Arguments, **kwargs

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# def my_function(**kid):
#   print("His last name is " + kid["lname"] + " He is "+ kid["age"] +" years young")

# my_function(fname = "Tobias", age = "12", lname = "Refsnes")
# ---------------------------------

# Default Parameter Value

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")
# my_function("South Ahh")
# ---------------------------------------------

# Passing a List as an Argument
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# snacks = ["biscuits", "sweets", "biltong"]
# my_function(snacks)
# my_function(fruits)
# ---------------------------------------------
# The return value
# def my_function(x):
#   return 5 * x * 5

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# ---------------------------------------

# Pass statement
# def myfunction():
#   pass





    # i = int(input())
# edit the code from the lines below
# i =0
# while i <=9 :
#     i = i+1
#     print(i)


# ---------------------------------------------
# Either type of loop will work. Example using a for loop:


# Example using a while loop:

# num = 0
# while num <= 1000:
#     print(num)
#     num += 1

# ----------counting from -10 to -1-----------------



# for num in range(-10, 0):
#     print(num)


# The len() function can be used for this purpose.

# Example:

# a_lst = ["a", "b", "c", "d"]
# print(len(a_lst)) # Prints 4

# ------------------task attempt-------------------------------

# # Hint: pattern contains 5 rows
# row = int(input())
# # start: 1
# # stop: row+1 (range never include stop number in result)
# # step: 1
# # run loop 5 times
# for i in range(row):
#     # Run inner loop i+1 times
#     for j in range(i+1):
#         print(j+1, end=' ')
#     # empty line after each row
#     print("")
# --------------REversing a number in python-----------------------------
# num =123
# reverse_number = 0

# while num > 10 :#Type in your code here 
#    #And here
#    digit = num % 10
#    reverse_number = reverse_number * 10 + digit
#    num = num
#    --------------------------------------------------------------------------
# print("Reverse Number ", reverse_number)


# ------------expected answer------------
# num = int(input())
# reverse_number = 0

# while num > 0:#Type in your code here
#     remainder = num%10
#     reverse_number = (reverse_number * 10 ) + remainder
#     num = num//10
# print("Reverse Number ", reverse_number)
# --------------------------------------------



# s: store sum of all numbers
# s = 0
# n = int(input())
# # run loop n times
# # stop: n+1 (because range never include stop number in result)
# for i in range(1,n+1,n):
#     # add current number to sum variable
#     s =+ n +i
# print("Sum is: ", s)

# ----------------------------------------------------------------


# adding numbers in a range 

# s: store sum of all numbers
# s = 0
# n = 10
# run loop n times
# stop: n+1 (because range never include stop number in result)
# for i in range(1,n+1,1):
    # add current number to sum variable
    
#     s += i
# print("Sum is: ", s)
# ------------------------------------------


# student_record = (1, "Charles", 23)
# print(student_record[1])
# --------------------------------------

# tuples

# veggies = ("mielie", "carrot")
# veggies = veggies + ("potato",)

# print(veggies)



# print("tomato" in veggies)


# print("mielie" in veggies)


# # -------------------------
# age = "ten"

# # tuple(age) 
# print(age)
# --------


# LISTS
# a shopping list

# groceries = ["bread", "eggs", "milk"]


# print(groceries[2])



# print("oats" in groceries)
# print("eggs" in groceries)



# QUIZ QUESTION
# Create a program where after the for loop has completed printing from 0 to any given number between 1 and 5, it displays the message "Done" using the else block

# For example, after a user enters 4 as input, the output should be the following:

# 0
# 1
# 2
# 3
# 4
# Done!

# --------------MY solution-------------

# n = "Done!"
# for i in range(0,2,1):
#     print(i)
# else: print(n)    

# -------------Expected solution---------

# n = int(input())
# for i in range(n+1):
#     print(i)
# else:
#     print("Done!")

# --------------Quiz Question------------------------
# Write code that iterates through and prints unlimited lines of STDIN until ~BREAK~ is seen.

# Sample STDIN
# The first line
# The second line
# The third line
# ~BREAK~

# Sample STDOUT
# The first line
# The second line
# The third line


# -----------------My Solution-----------
# Your code here!
# while True:
#     n = input() # This gets STDIN
#     if n == "~BREAK~":
#          break
#     print(n)
# ------------Quiz Question----------------
# Create a Python program that prints all the numbers from 0 to 4 except two distinct numbers entered by the user.
# Note : Use 'continue' statement.

# If user input is
# 3
# 2

# Expected Output :
# 0 1 4

# # -----------attemt-----------
# num1 = int(input())
# num2 = int(input())

# for x in range(0,5,1):
#     while 
#     if x == num1 and x == num2:
#         continue
#     print(x)

# -----------Review Question--------
# Write a function that returns "a is greater than b", "a is less than b", or "a is equal to b" depending on the values of two int input params a and b.

# STDIN Format
# a b (example 1 15 where a=1 and b=15)

# Sample STDIN/STDOUT
# 1 3 / a is less than b
# 3 3 / a is equal to b
# 7 3 / a is greater than b

# ---------------------Attempt------------------------
# def a_vs_b(a,b):
# 	# your code here
# 	if a>b:
# 	    return "a is greater than b"
# 	elif a<b:
# 	    return "a is less than b"
#     elif a<b:
# 	    return "a is equal to b"
# # Input handling, do not modify!
# input_parts = input().split(" ")
# a = int(input_parts[0])
# b = int(input_parts[1])
# print(a_vs_b(a, b))

# -----------Review Question--------
# Write a function that converts an int num between 0-9 (inclusive) to its string equivalent (i.e., 1 -> "one").

# Use an if/elif/else statement in your solution.

# Sample STDIN/STDOUT
# 1 / one
# ---------------------Attempt------------------------
# def int_to_string(num):
#     # Your code here
#     if num == 0:
#         return "zero"
#     elif num == 1:
#         return "one" 
#     elif num == 2:
#         return "two" 
#     elif num == 3:
#         return "three" 
#     elif num == 4:
#         return "four" 
#     elif num == 5:
#         return "five" 
#     elif num == 6:
#         return "six" 
#     elif num == 7:
#         return "seven" 
#     elif num == 8:
#         return "eight" 
#     elif num == 9:
#         return "nine" 
#     else:
#         return "Invalid input" 
    

# # Input handling, do not modify!
# num = int(input())
# print(int_to_string(num))


# ---------------Review Question----------------------
# Write a function that prints out every number from 0 to an input parameter n (inclusive).

# Use a for loop in your solution.

# Sample STDIN
# 3

# Sample STDOUT
# 0
# 1
# 2
# 3
# ---------------------Attempt------------------------

# def zero_to_n(n):
# 	# Your code here
# 	for i in range(n+1):
# 	    print(i)
	

# # Input handling, do not modify!
# n = int(input())
# zero_to_n(n)

# ---------------Review Question----------------------
# Write a program to create a function that takes two arguments as user input, name and age, and print their value.

# Test your program by using as input one of the following at a time:

# John
# 55

# To get the output:

# Name:

# Age:

# John 55

# James
# 30

# To get the output:

# Name:

# Age:

# James 30

# Jill
# 45

# To get the output:

# Name:

# Age:

# Jill 45

# Make sure you DO NOT have any spaces after Name: and Age:

# ---------------------Attempt------------------------

# ????????????????????????????


# --------Review Question----

# Below is the function display_student(name, age). Assign a new name show_student(name, age) to it and call it using the new name.
# Given:

# def display_student(name, age):
#     print(name, age)

# display_student("Emma", 26)
# You should be able to call the same function using
# show_student(name, age)

# Make sure in your solution code that you only call the show_student() function
# Use the name Emma and age 26 in your test data. Add a new line after each test input in STDIN

# ------------------Attempt------------------------

# ---------Review Question ---------------------------
# Write a program to create a function called show_employee() .
# It should accept the employee’s name and salary as user input and display both.

# Use Ben 2000 as your test data
# Input:

# "Ben"
# 12000

# Expected output:

# Name: Ben salary: 12000


# ---------------Attempt--------------


# --------------------------------
# List functions

# Python supplies several built-in methods that can be used to modify lists. Let’s go over a few of them.
# append()

# append() adds an object to the end of a list:

a = ['a','b']
a.append(123)
print(a)