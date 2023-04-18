


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

def my_function(**kid):
  print("His last name is " + kid["lname"] + " He is "+ kid["age"] +" years young")

my_function(fname = "Tobias", age = "12", lname = "Refsnes")
