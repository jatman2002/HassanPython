import random

# for i in range(0,100):
#     x = random.randint(0,10)
#     print(x)

def print_hello():
    print('Hello')

def add_1(number):
    result = number + 1
    print(result)

add_1(random.randint(0,19))
add_1(10)

def add(number_1, number_2):
    result = number_1 + number_2
    return result

r = add(5, 6)
print(r)

# for i in range(0,10):
#     print_hello()


def cms_to_inch(cm):
    conversion_factor = 2.54
    inches = cm / conversion_factor
    conversion_factor=3
    print(conversion_factor)
    return inches


# print(cm)
print(cms_to_inch(10))
print(cms_to_inch(15))


global_variable = 18

def fucntion():
    print(global_variable)

print('hello')

fucntion()



#########################

number = 1
# if(number >= 5 and number <= 10):
#     print('True')
# else:
#     print('False')

# if(type(number) == )

string = 'asbdsijgs'

if(len(string) == 9):
    print(True)

user_input = input("Enter a number: ")
if (user_input == ''):
    print("Theres nothing here!")
else:
    as_an_int = int(user_input)

# format check