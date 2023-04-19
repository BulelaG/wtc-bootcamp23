


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
student_record = (1, "Charles", 23)
print(student_record)