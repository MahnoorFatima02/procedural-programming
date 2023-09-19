import random


# Question # 2: Many sided roll playing dice

def multi_dice_roll(number):
    return random.randint(1, number)


if __name__ == "__main__":
    maximum_no_of_dice_sides = int(input("Maximum sided dice you want to roll: "))
    current_dice_sides = 0
    while current_dice_sides != maximum_no_of_dice_sides:
        current_dice_sides = multi_dice_roll(maximum_no_of_dice_sides)
        print("Dice roll value is ", current_dice_sides)
