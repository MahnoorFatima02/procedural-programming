import random
import math

# Question 1: Number divisible by 3

x = 1
while x < 1000:
    if x % 3 == 0:
        print(f"This number is divisible by 3: {x}")
    x += 1

# Question 2: Inches to Centimeters

inches_to_centimeters_conversion = 2.54
while True:
    inches_value = float(input("Please enter your inches value here: "))
    if inches_value > 0:
        centimeters_value = inches_value * inches_to_centimeters_conversion
        print(f"The value in centimeters is: {centimeters_value}")
    else:
        print("Cannot calculate negative inputs.")
        break

# Question 3: Biggest and smallest integers

numbers_list = []
user_input = "test"
while user_input != "":
    user_input = input("Please enter your numbers here: ")
    if user_input == "":
        print("Now you have choose to quit by entering an empty string!!")
    else:
        number = int(user_input)
        numbers_list.append(number)


biggest_number_in_list = max(numbers_list)
smallest_number_in_list = min(numbers_list)

print(f"The biggest number entered was: {biggest_number_in_list}")
print(f"The smallest number entered was: {smallest_number_in_list}")

# Question 4

random_number = random.randint(1, 10)
guess_number = 0
while int(guess_number) != random_number:
    guess_number = input("Please enter your number: ")
    if int(guess_number) > random_number:
        print("Your number was too high")
    elif int(guess_number) < random_number:
        print("Your number was too low")
    else:
        print("Correct!!")

# Question 5: Username and password

standard_user_name = "python"
standard_user_password = "rules"

x = 0
while x < 5:
    user_name = input("Please enter your user name here: ")
    user_password = input("Please enter your password here: ")
    x = x + 1
    if x >= 5:
        print("Access denied!!")
    elif user_name == standard_user_name and user_password == standard_user_password:
        print("Welcome!!")
        break
    else:
        print("Invalid credentials")


#  # Question 6: Value of pi

square_random_number_points_N = int(input("Please enter number of points you want to add: "))
circle_random_points_n = 0
for i in range(square_random_number_points_N):
    x = random.uniform(1, -1)
    y = random.uniform(1, -1)

    if x ** 2 + y ** 2 < 1:
        circle_random_points_n += 1

approx_pi_value = 4 * (circle_random_points_n / square_random_number_points_N)

print(round(approx_pi_value, 2))
