# import random

# # for i in range(0,100):
# #     x = random.randint(0,10)
# #     print(x)

# def print_hello():
#     print('Hello')

# def add_1(number):
#     result = number + 1
#     print(result)

# add_1(random.randint(0,19))
# add_1(10)

# def add(number_1, number_2):
#     result = number_1 + number_2
#     return result

# r = add(5, 6)
# print(r)

# # for i in range(0,10):
# #     print_hello()


# def cms_to_inch(cm):
#     conversion_factor = 2.54
#     inches = cm / conversion_factor
#     conversion_factor=3
#     print(conversion_factor)
#     return inches


# # print(cm)
# print(cms_to_inch(10))
# print(cms_to_inch(15))


# global_variable = 18

# def fucntion():
#     print(global_variable)

# print('hello')

# fucntion()



# #########################

# number = 1
# # if(number >= 5 and number <= 10):
# #     print('True')
# # else:
# #     print('False')

# # if(type(number) == )

# string = 'asbdsijgs'

# if(len(string) == 9):
#     print(True)

# user_input = input("Enter a number: ")
# if (user_input == ''):
#     print("Theres nothing here!")
# else:
#     as_an_int = int(user_input)

# # format check


print('-'*100)

### Generating Random Numbers
##  To do this in Python we first need to import the random library (this is always done at the top of your Python file)
import random
import math # Ignore this, its for later

##  We then can use the randint(start_of_range, end_of_range) function in the random library to generate our random number
random_number = random.randint(1,10)
print(f'{random_number=}')

print('-'*100)
### Procedures

##  A procedure is a block of code that can be run several times without needed to repeat the entire block
##  It can take in a set of parameters (0+)
##  You can think of it as some black box (abstraction), you only need to know what the procdure does and what parameters it needs, not the specifics of how it works
##                     ------------
##     x = {}         |            |
##     y = {} ------> |  p(x,y,z)  |
##     z = {}         |            |
##                     ------------


##  Syntax is
##  def procedure_name(parameter_1, ..., parameter_n):
##      {code}
##  {main code}
##  e.g. a procedure that takes in a 2-D list and prints it out as a grid

#   This is our procedure
def print_list_as_grid(li):
    for row in li:
        print(row)

#   We define our 2-D list and then invoke (call) the procudure and pass in the list we want to use
two_d_list = [[1,2,3],[4,5,6],[7,8,9]]
print_list_as_grid(two_d_list) # so here we are saying run the code in the procedure using two_d_list wherever li is used
print() # blank line

#   We can do it as many times as we want with whatever 2-D list we want
another_two_d_list = [[9,8,7],[6,5,4],[3,2,1]]
print_list_as_grid(another_two_d_list)

print('-'*100)

### Functions

##  A function is simply a procedure that returns something
##                     ------------
##     x = {}         |            |
##     y = {} ------> |  p(x,y,z)  | ------> {some value}
##     z = {}         |            |
##                     ------------

##  The syntax for this is the same as before but at the end of the function, you add
##  return {value}

##  Lets make a pythagoras calculator
##      - It should take in two parameters a and b which are integers
##      - It should perform a^2 + b^2 in order to find some c^2
##      - It should apply square root to get c
##      - c should be returned

def pythagoras(a, b):
    a_squared = a * a # Note you can also use the ^ operator and do a^2 (I just prefer a*a)
    b_squared = b * b
    c_squared = a_squared + b_squared
    c = math.sqrt(c_squared)
    return c


number_1 = 10
number_2 = 15
result = pythagoras(number_1, number_2)
print(f'{pythagoras(number_1, number_2)=}')
print() # blank line

number_1 = 3
number_2 = 4
result = pythagoras(number_1, number_2)
print(f'{pythagoras(number_1, number_2)=}')

print('-'*100)

### Local and Global variables

##  To put it simply, a local variable is one that is defined within a procedure/function
##  If we try to use a local variable outside of its scope (the function its defined in, python throws an error and crashes the program)
##  The benefit of this is that things start to become encapsulated (basically self-contained)
##  We ideally want to minimise trying to access things outside of a scope in order to improve reusability of code (the whole reason for using procedures and functions)
##  Looking at the code above, c and c_squared are examples of local variables

##  Global variables are the opposite
##  They are defined in the main code
##  They can be accessed anywhere and at anytime
##  Examples being two_d_list and number_1


### Validation

##  Range check
#   Checking if a number is within a certain range
number_to_check = 6
if 3 <= number_to_check and number_to_check <= 10:
    print(f'{number_to_check} is between 3 and 10!')
else:
    print(f'{number_to_check} is not between 3 and 10 :/')

##  Type check
#   Checking the type of a variable/value
string = "This is a string"
if type(string) == str:
    print("The variable string is of type string")
else:
    print("The variable string is not of type string")

##  Length check

some_list = [1,2,3,4]
if len(some_list) == 3:
    print("some_list has length 3")
else:
    print("some_list does not have length 3")

##  Presence check

input_string = "" # assume a user did not type anything and just hit the enter key
if input_string == "": # basically checking if it is empty
    print("This is empty")