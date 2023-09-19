import random


# Question # 1 : Random dice roll

def random_roll_dice():
    return random.randint(1, 6)


if __name__ == "__main__":
    dice_roll_value = 0
    while dice_roll_value != 6:
        dice_roll_value = random_roll_dice()
        print("Dice roll value is ", dice_roll_value)
