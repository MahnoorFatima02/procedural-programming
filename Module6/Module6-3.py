# Question # 3: gallons to litres conversion

def gallons_to_litres(gallon_value):
    litres_value = round(gallon_value * 3.78, 2)
    return litres_value


if __name__ == "__main__":
    value_to_convert = int(input("Please enter your gallon value here: "))
    if value_to_convert > 0:
        value_to_convert = gallons_to_litres(value_to_convert)
        print("Your value in litres is: ", value_to_convert)
