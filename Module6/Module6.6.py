import random
import math


# Question # 6
def calculate_price_per_sq_meter(diameter, price):
    centimeter_to_meter = diameter * 0.01
    area = ((centimeter_to_meter / 2) ** 2) * math.pi
    price_per_square_meter = price / area
    return price_per_square_meter


if __name__ == "__main__":
    number_of_inputs = 0
    optimal_pizza_price = []
    while number_of_inputs < 2:
        pizza_diameter = int(input("Enter the diameter of your pizza here: "))
        pizza_price = int(input("Enter the price of your pizza here: "))
        price_estimation = calculate_price_per_sq_meter(pizza_diameter, pizza_price)

        optimal_pizza_price.append(price_estimation)
        number_of_inputs = number_of_inputs + 1

    if optimal_pizza_price[0] < optimal_pizza_price[1]:
        print("Your pizza option 1 is better than pizza option 2")
    else:
        print("Your pizza option 2 is better than pizza option 1")
