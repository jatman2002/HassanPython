print("-"*100)

### Variable assignment ###

##  We can assign a value of any data type to a variable
##  (and give it any name we want)
##  The values stored in these variables can be changed at any time during a program
##  (see Lesson2.py under Sequence)
##  (or the Operators section below)

#   Integer (whole number, can be negative)
number_variable = 10 
print(f'{number_variable=}\t{type(number_variable)}\n')

#   Float / real (any number - positive, negative with decimal)
float_variable = 2.0
print(f'{float_variable=}\t{type(float_variable)}\n')

#   Character:
character_variable = 'a'
print(f'{character_variable=}\t{type(character_variable)}\n')

#   String (collection of characters):
string_variable = "abcd"
print(f'{string_variable=}\t{type(string_variable)}\n')

#   Boolean (True or False):
boolean_variable = True
print(f'{boolean_variable=}\t{type(boolean_variable)}\n')

#   List (collection of any of the same data type)
#   note: does not need to be in order
list_of_numbers = [4,1,5,2,3]
print(f'{list_of_numbers=}\t{type(list_of_numbers)}\n')

list_of_string = ["abcd", "efgh", "ijkl"]
print(f'{list_of_string=}\t{type(list_of_string)}\n')

print("-"*100)


### Constants ###

##  Constants are like variables except that their values 
##  cannot be changed while the program is running



### Operators ###

##  Mathematical operators

#   Feel free to change these and see the outcomes (just don't let num2 be 0)
num1 = 10
num2 = 4

#   Addition
result = num1 + num2
print("num1 + num2 = ")
print(result)
print()

#   Subtraction
result = num1 - num2
print("num1 - num2 = ")
print(result)
print()

#   Multipliction
result = num1 * num2
print("num1 * num2 = ")
print(result)
print()

#   Division
result = num1 / num2
print("num1 * num2 = ")
print(result)
print()

#   Exponent (to the power of)
result = num1 ^ num2
print("num1 ^ num2 = ")
print(result)
print()

#   Integer Division (Basically round down)
result = num1 // num2
print("num1 // num2 = ")
print(result)
print()

#   Modulus (Get the remainder)
result = num1 % num2
print("num1 % num2 = ")
print(result)
print()


print("-"*100)


##  Boolean Operators
##  These all return a boolean value

#   Comparitive operators
#   Less than <, greater than >
result = num1 > num2
print("num1 > num2")
print(result)
print()

result = num1 < num2
print("num1 < num2")
print(result)
print()

#   Less/greater than or equal to
result = num1 >= num2
print("num1 >= num2")
print(result)
print()

result = num1 <+ num2
print("num1 <= num2")
print(result)
print()

#   Equal to ==
result = num1 == num2
print("num1 == num2")
print(result)
print()


##  Logical Operators

a = True
b = False

#   AND
#   If we have input a and b (T - true, F - false)
#    a | b | a AND b 
#   ---+---+---------
#    F | F |    F
#    F | T |    F
#    T | F |    F
#    T | T |    T

result = a and b
print("a and b")
print(result)
print()

#   OR
#   If we have input a and b (T - true, F - false)
#    a | b | a OR b 
#   ---+---+--------
#    F | F |   F
#    F | T |   T
#    T | F |   T
#    T | T |   T

result = a or b
print("a or b")
print(result)
print()


#   NOT
#   If we have input a (T - true, F - false)
#    a | NOT a
#   ---+-------
#    F |  T 
#    T |  F

result = not a
print("not a")
print(result)
print()


print("-"*100)
print()

### Strings ###

##  Strings are defined using double-quotes as shown:
string_variable = "Hello World!"

##  Indexing

#   We can retrieve a character at a specific index (position) using var[i]
#   where var is the variable containing the string and i is the index
#   remember, positions start at 0 not 1!!

specific_character = string_variable[4]
print("string_variable[4]")
print(specific_character)
print()

#   If the position specified is greater than or equal to the length then the program crashes
#   We can get the length by using the len() function
length_of_string = len(string_variable)
print(f'{length_of_string=}')
#   Uncomment the below line to observe the crash
# error_character = string_variable[length_of_string]

##  Substrings

#   Using the idea of indexes, we can retrieve a section of the string called a substring
#   We do this by var[i:j] where
#   -   var is the string variable
#   -   i is the starting index
#   -   j is the index after the final index
substring = string_variable[0:4]
print(f'{substring=}\n')

##  Concatenation

#   This is the joining of two strings
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + string2
print(f'{concatenated_string=}\n') 
# notice how there is no space between the words? 
# That's because there isn't a space in the strings!


## Character sets

character_variable = 'A'

#  To convert a charcater into its ascii value, we use the ord() function
ascii_value = ord(character_variable)
print(f'{ascii_value=}')

#   To convert it back, we can use the chr() function
back_to_character = chr(ascii_value)
print(f'{back_to_character=}')
print(f'{character_variable==back_to_character=}\n')

print("-"*100)
print()


### Data Validation

##  Now lets say we have a program where the user can enter a number
##  In Python, the input() allows the user to enter something
##  However, this returns a string
##  If we tried to use the value as an integer, the program would break
##  Uncomment the code snippet below to see this:

# some_string = "10"
# number = some_string + 10 # this is where it will break and say you cannot add a string an integer

##  In a real program, any form of external input creates a weak point
##  This could be user entering some text, selecting something on the screen
##  could even be the program reading some file

##  To fix this we can do something call type casting
##  This involves converting a data type into another data type
##  (Only if possible!!)

#   String to integer
some_string = "10"
print(f'{some_string=}\t\t{type(some_string)=}')
some_string_as_int = int(some_string)
print(f'{some_string_as_int=}\t\t{type(some_string_as_int)=}\n')

# error case:
# some_string = "abcd"
# some_string_as_int = int(some_string)

#   Integer to string uses the str() function
