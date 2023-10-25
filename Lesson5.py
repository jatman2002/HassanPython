# question from past paper

number_of_items_sold = int(input("How many items were sold : "))
number_of_years_employed = int(input("How many years employed :"))
if number_of_years_employed <= 2 and number_of_items_sold > 100:
    bonus = number_of_items_sold*2
elif number_of_years_employed > 2:
    bonus = number_of_items_sold*10
else:
    bonus = 0
print(bonus)



