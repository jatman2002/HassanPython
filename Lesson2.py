print('-'*100)

### Sequencing

# Sequencing is simply the order in which a set of states occur, e.g.
# In this example we:
#  - Assign 10 to a variable
#  - Add 10 to it
#  - Divide it by 4
#  - Apply modulus 5 (get the remainder when dividing by 5)
number_variable = 10
number_variable = number_variable + 10
number_variable = number_variable / 4
number_variable = number_variable % 5
print(f'{number_variable=}')

print('-'*100)

### Selection

condition1 = False
condition2 = True

if condition1 == True:
    print(f'{condition1=}')
elif condition2 == True:
    print(f'{condition2=}')
else:
    print("All false")

print('-'*100)

# Remember that we can use the logical operators from Lesson 1 as well
# e.g. if ((num1 == 10) or (num1 == 5)) and ((num2 == 12) or (num2 == 29))

### Iteration

##  Definite Iteration

# The syntax for this is:
# for index_variable in range(start_index, end_index + 1):
#     {code}

# To print the numbers from 0 to 9 and the value :
for i in range(0,10):
    print(i)

print('-'*100)

# Loops can be used for various things as you can add any block of code inside the loop
# e.g. print the first 10 multiples of 10
for i in range(1,11):
    print(f'10 x {i} =\t{i*10}')

print('-'*100)

##  Indefnite Iteration

# These are condition based loops, they only end when a certain condition is met
# while condition == True:
#     {code}

# e.g. increase a counter and stop when it reaches 5
counter = 0
while counter < 5:
    counter = counter + 1
print(f'{counter=}')

print('-'*100)

### Lists / Arrays

# We already covered the basics of lists when talking about strings in Lesson 1
# Same concepts apply, indexing, substring (in this case its sublist)
# Note, no concatenation though

##  List Iteration

# Lets say we have a list and we want to perform some calculations using each element in the list
# We can combine the idea of indexes and for loops to do this
# We need the length for this
number_list = [4,2,7,12,5,2] # Note that lists aren't required to have unique elements
length = len(number_list)
print(f'{length=}')
for i in range(0, length):
    print(f'number_list[{i}]= {number_list[i]}')

print('-'*100)

##  2-D Lists / Arrays

# This is where each 'element' in a list is another list
# An example could be a grid for some board game, marking each 'cell' with a set of 2-D coordinates

two_d_list = [[1,2,3], [4,5,6], [7,8,9]]

# The syntax for getting a value in a 2-D list is: 
# var[i][j] where i is the position of a list in var and j the element in the list
value = two_d_list[0][2]
print(f'{value=}')
print()

# If we perform basic iteration like above, we can see how it is structured
for i in range(len(two_d_list)):
    print(f'two_d_list[{i}]= {two_d_list[i]}   its type is --> {type(two_d_list[i])}')
print()

# Lets say we want to access each element one by one systematically
# We can nest two for loops, the first one will retrieve each list in two_d_list and the second will access each element

for row_index in range(0, len(two_d_list)):
    row = two_d_list[row_index]
    for column_index in range(0, len(row)):
        element = two_d_list[row_index][column_index]
        print(f'two_d_list[{row_index}][{column_index}]= {element}')