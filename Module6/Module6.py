import random
import math


# Question # 1 : Random dice roll

# def random_roll_dice():
#     return random.randint(1, 6)
#
#
# def main():
#     dice_roll_value = 0
#     while dice_roll_value != 6:
#         dice_roll_value = random_roll_dice()
#         print("Dice roll value is ", dice_roll_value)
#
#
# if __name__ == "__main__":
#     main()


# Question # 2: Many sided roll playing dice
#
# def multiple_sided_dice(number):
#     return random.randint(1, number)
#
#
# def main():
#     maximum_no_of_dice_sides = int(input("Maximum sided dice you want to roll: "))
#     current_dice_sides = 0
#     while current_dice_sides != maximum_no_of_dice_sides:
#         current_dice_sides = multiple_sided_dice(maximum_no_of_dice_sides)
#         print("Dice roll value is ", current_dice_sides)
#
#
# if __name__ == "__main__":
#     main()


# # Question # 3:

# def gallons_to_litres_conversion(gallon_value):
#     litres_value = gallon_value * 3.78
#     return litres_value


# def main():
#     value_to_convert = int(input("Please enter your gallon value here: "))
#     if value_to_convert > 0:
#         value_to_convert = gallons_to_litres_conversion(value_to_convert)
#         print("Your value in litres is: ", value_to_convert)
#
#
# if __name__ == "__main__":
#     main()

# Question # 4: sum of list of integers
#
# def sum_of_list(numbers):
#     sum_of_numbers = 0
#     for i in numbers:
#         sum_of_numbers = sum_of_numbers + i
#     return sum_of_numbers


# def main():
#     integer_list = []
#     max_number_of_input = 6
#     while len(integer_list) < max_number_of_input:
#         integer_value = int(input("Please enter integer to add into list: "))
#         integer_list.append(integer_value)
#
#     sum_of_integers = sum_of_list(integer_list)
#     print("The sum of list of integers is ", sum_of_integers)
#
#
# if __name__ == "__main__":
#     main()


# Question # 5:

# def original_list(iterable):
#     s = 0
#     result = []
#     iterable = [2, 3, 4, 5, 6, 7, 8]
#     for value in iterable:
#         s += value
#         result.append(s)
#     return result
#
#
# def cut_down_list():
# #     new_list = []


# Question # 6
# def price_per_sq_meter(diameter, price):
#     centimeter_to_meter = diameter * 0.01
#     area = ((centimeter_to_meter / 2) ** 2) * math.pi
#     price_per_square_meter = price / area
#     return price_per_square_meter
#
# if __name__ == "__main__":
#     number_of_inputs = 0
#     optimal_pizza_price = []
#     while number_of_inputs < 2:
#         pizza_diameter = int(input("Enter the diameter of your pizza here: "))
#         pizza_price = int(input("Enter the price of your pizza here: "))
#         price_estimation = price_per_sq_meter(pizza_diameter, pizza_price)
#
#         print("The price per sq meter of your pizza is: ", price_estimation)
#         optimal_pizza_price.append(price_estimation)
#         number_of_inputs = number_of_inputs + 1
#
#     print("BEST PIZZA IN PRICE PER SQUARE METER IS ", min(optimal_pizza_price))