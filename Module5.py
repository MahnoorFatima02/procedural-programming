import random

# Question# 1: Dices to roll

sum_of_dice = 0
no_of_dices_to_roll = int(input("Enter how many dices to roll: "))
for i in range(0, no_of_dices_to_roll):
    dice_value = random.randint(1,6)
    sum_of_dice = dice_value + sum_of_dice

print(sum_of_dice)


# Question # 2: sort 5 numbers in descending order

numbers_list = []
input_numbers = "test"
while input_numbers != "":
    input_numbers = input("Please enter your numbers here: ")
    if input_numbers != "":
        numbers_list.append(int(input_numbers))

numbers_list.sort(reverse=True)
print(f"First 5 values in sorted list (in Descending) are", numbers_list[0:5])

# Question # 3
# Program to check if a number is prime or not

num = int(input("Enter a number: "))
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# Question # 4: Cities name

cities_list = []
for i in range(0, 5):
    cities_name = input("Enter your cities name here: ")
    cities_list.append(cities_name)

for city in cities_list:
    print(city)
