### Variable assignment ###

##  We can assign a value of any data type to a variable
##  (and give it any name we want)
##  The values stored in these variables can be changed at any time during a program
##  (see Lesson2.py under Sequence)
##  (or the Operators section below)

#   Integer:
number_variable = 10 

#   Float / real:
float_variable = 2.0

#   Character:
character_variable = 'a'

#   String (collection of characters):
string_variable = "abcd"

#   Boolean (True or False):
boolean_variable = True

#   List (collection of any of the same data type)
#   note: does not need to be in order
list_of_numbers = [1,2,3,4,5]
list_of_string = ["abcd", "efgh", "ijkl"]



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


### Strings ###