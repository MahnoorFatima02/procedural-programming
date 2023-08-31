import math
from random import randint, randrange

# Question 1
your_name = input("Enter your name here: ")
print("Hello, " + your_name + "!")

# Question 2: Area of circle
circle_radius = input("Enter radius of circle here: ")
radius_square = float(circle_radius) ** 2
circle_area = round(radius_square * math.pi, 2)
print("Area of circle is " + str(circle_area))

# Question 3: Area and Perimeter of Rectangle
rectangle_length = input("Enter length of rectangle here: ")
rectangle_width = input("Enter width of rectangle here: ")
rectangle_area = round(float(rectangle_length) * float(rectangle_width), 2)
rectangle_perimeter = round(2 * (float(rectangle_length) + float(rectangle_width)), 2)
print("The area of rectangle is " + str(rectangle_area))
print("The perimeter of rectangle is " + str(rectangle_perimeter))

# Question 4: Integer number
numbers = []
for x in range(1, 4):
    number = input("Please enter your number here: ")
    numbers.append(int(number))

sum_of_numbers = 0
product_of_numbers = 1
for x in numbers:
    sum_of_numbers = x + sum_of_numbers
    product_of_numbers = x * product_of_numbers

average_of_numbers = round(sum_of_numbers / len(numbers), 2)

print("The sum of integers is: " + str(sum_of_numbers))
print("The product of integers is: " + str(product_of_numbers))
print("The average of integers is: " + str(average_of_numbers))

# Question 5: mass into kilograms and grams
talents_mass = input("Enter your mass in talents(leiviskä): ")
pounds_mass = input("Enter your mass in pounds(naula): ")
lots_mass = input("Enter your mass in lots(luoti): ")
talent_to_pound = float(20)
pound_to_lot = float(32)
lot_to_gram = float(13.3)

talents_to_grams_conversion = float(talents_mass) * talent_to_pound * pound_to_lot * lot_to_gram
pounds_to_grams_conversion = float(pounds_mass) * pound_to_lot * lot_to_gram
lot_to_gram_conversion = float(lots_mass) * lot_to_gram

total_grams = round(talents_to_grams_conversion + pounds_to_grams_conversion + lot_to_gram_conversion, 3)

print(total_grams)
grams_to_kilograms_conversion = total_grams / 1000
kilogram = grams_to_kilograms_conversion // 1
gram = round(grams_to_kilograms_conversion % 1, 6) * 1000
print("The weight in modern units: \n" + str(kilogram) + " Kilograms and " + str(gram) + " grams")

# Question 6: random combination numbers
n = 3
print(''.join(["{}".format(randint(0, 9)) for i in range(0, n)]))
n = 4
print(''.join(["{}".format(randint(1, 6)) for y in range(0, n)]))




