# num1 = 5
# print(num1==10)

# num2 = 5

# addition = num1+num2
# remainder = addition % 2

# if ((num1+num2) % 2) == 0:
#     print("even")

# if remainder==1:
#     print("addition is odd")
# elif remainder==0:
#     print("addition is even")
# else:
#     print("not 10")

    # print("not indent")

    # number = 3

    # if number % 3 == 0 and number % 5 == 0:
    #     print("fizz buzz")


# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))

# if num2 == 0:
#     print("Try again, num2 is 0")
# else:
#     print(num1/num2)


num_list = [1,2,3,4,5,6]
num_list[3]

# for i in range(6):
#     result = num_list[i] * 10
#     print(result)

# for x in range(11):
#     print(x)

# counter = 0
# is_done = False

# while not is_done:
#     print(counter)
#     counter = counter + 1


li = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

for row_index in range(len(li)):
    row = li[row_index]
    for column in range(len(row)):
        print("row: " + str(row_index) + "\t col: " + str(column))
        # print(li[row_index][column])
